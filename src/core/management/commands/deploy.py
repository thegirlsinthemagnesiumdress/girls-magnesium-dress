import os
from os.path import dirname, join
from subprocess import check_output, check_call, CalledProcessError

from django.core.management import call_command
from django.core.management.base import BaseCommand

from djangae.environment import get_application_root
from google import appengine

APP_CFG = join(dirname(dirname(appengine.__path__[0])), "appcfg.py")

APP_YAML = os.path.join(get_application_root(), "app.yaml")

STAGING_APP_ID = 'talent-revolution-staging'


def update_version_in_app_yaml():
    revision = check_output(["git", "rev-parse", "HEAD"])
    branch = check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])

    new_version = "-".join([
        revision[:10],
        branch[:6]
    ])

    with open(APP_YAML, "r") as f:
        output = []
        for line in f:
            if line.startswith("version:"):
                try:
                    current_version_number = int(line.split(":")[-1].split("-")[0].lstrip())
                except (TypeError, ValueError):
                    current_version_number = 0

                current_version_number += 1

                new_version = "%s-%s" % (current_version_number, new_version)
                line = "version: %s\n" % new_version
            output.append(line)

    open(APP_YAML, "w").writelines(output)


def run_deployment(application, version):
    call_command("collectstatic", interactive=False)
    call_command("assets", "build")

    command = [APP_CFG, "update", "src/"]
    if application:
        command.extend(["--application", application])

    if version:
        command.extend(["--version", version])
    command.extend(["--oauth2"])

    check_call(command)


def reset_app_yaml():
    check_call(["git", "checkout", APP_YAML])


def commit_app_yaml():
    check_call(["git", "add", APP_YAML])
    check_call(["git", "commit", "-m", "Version for deployment to live"])


def update_indexes():
    command = [APP_CFG, "update_indexes", "src/"]
    check_call(command)


def deploy_to_staging(version):
    run_deployment(STAGING_APP_ID, version)


def deploy_to_live(version):
    run_deployment(application=None, version=version)


class Command(BaseCommand):
    help = 'Deploys a new version of the Franz app'

    def add_arguments(self, parser):
        parser.add_argument('--only-staging', action='store_true', default=False)
        parser.add_argument('--only-live', action='store_true', default=False)

        parser.add_argument('--app-version', type=unicode, default=None)
        parser.add_argument('--app-version-staging', type=unicode, default=None)
        parser.add_argument('--disable-version-bump', action='store_true', default=False)
        parser.add_argument('--just-indexes', action='store_true', default=False)

    def handle(self, *args, **options):

        if options['just_indexes']:
            update_indexes()
            return

        if not options['only_live']:
            staging_version = options['app_version_staging'] if options['app_version_staging'] else 'master'
            self.stdout.write('Deploying to staging using version: "' + staging_version + '"')
            deploy_to_staging(staging_version)
            if options['only_staging']:
                self.stdout.write("Only staging was specified, skipping live deployment")
                return
        else:
            self.stdout.write("Only live was specified, skipping staging deployment")

        if options['app_version']:
            self.stdout.write("Version was specified, not bumping app.yaml version")
            options['disable_version_bump'] = True

        if not options['disable_version_bump']:
            update_version_in_app_yaml()

        try:
            deploy_to_live(options['app_version'])
            if not options['disable_version_bump']:
                commit_app_yaml()

        except CalledProcessError:
            if not options['disable_version_bump']:
                reset_app_yaml()
            raise
