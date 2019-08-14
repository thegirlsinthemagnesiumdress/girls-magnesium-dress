from django.conf import settings

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Build a new version of the DMB app'

    def handle(self, *args, **options):
        languages = [code for code, _ in settings.LANGUAGES]
        call_command("gulp", "build", settings=options['settings'])
        call_command("collectstatic", settings=options['settings'], interactive=False)
        call_command("compilemessages", locale=languages, settings=options['settings'])
