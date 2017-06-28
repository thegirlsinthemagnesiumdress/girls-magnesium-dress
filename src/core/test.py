import os
import mimetypes
import time
import subprocess

from nose.plugins import Plugin

from django.conf import settings
from django.http import HttpResponse, Http404
from django.test import LiveServerTestCase
from django.template import Template, Context
from django.test.utils import override_settings
from django.conf.urls import url

from djangae import environment

try:
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False


class WebdriverPlugin(Plugin):
    enabled = True

    def __init__(self, *args, **kwargs):
        super(WebdriverPlugin, self).__init__(*args, **kwargs)
        self._driver = None

    def configure(self, options, conf):
        pass

    def begin(self, *args, **kwargs):
        command = [
            settings.CHROMEDRIVER_PATH,
            "--port=4444",
            "--url-base=wd/hub"
        ]
        self._driver = subprocess.Popen(command, stdout=subprocess.PIPE)

    def finalize(self, *args, **kwargs):
        if self._driver:
            self._driver.terminate()


SPEC_RUNNER_HTML = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Jasmine Spec Runner v2.6.4</title>

  <link rel="stylesheet" href="{{STATIC_URL}}jasmine/lib/jasmine-core/jasmine.css">

  <script src="{{STATIC_URL}}jasmine/lib/jasmine-core/jasmine.js"></script>
  <script src="{{STATIC_URL}}jasmine/lib/jasmine-core/jasmine-html.js"></script>
  <script src="{{STATIC_URL}}jasmine/lib/jasmine-core/boot.js"></script>

  <!-- include source files here... -->
  {% for file in source_files %}
  <script src="{{file}}"></script>
  {% endfor %}

  <!-- include spec files here... -->
  {% for file in spec_files %}
  <script src="{{file}}"></script>
  {% endfor %}
</head>
<body>
{% if template_path %}
{% include template_path %}
{% endif %}
</body>
</html>
"""

urlpatterns = []


def _view_factory(source_files, spec_files, template_path):
    def view(request):
        template = Template(SPEC_RUNNER_HTML)

        return HttpResponse(template.render(Context({
            "source_files": source_files,
            "spec_files": spec_files,
            "template_path": template_path,
            "STATIC_URL": settings.STATIC_URL
        })))
    return view


def _serve(request, path, prefix=None):
    project_root = environment.get_application_root()
    full_path = os.path.join(project_root, path)
    if not os.path.exists(full_path):
        raise Http404()

    mimetype = mimetypes.guess_type(full_path)
    with open(full_path, "r") as f:
        data = f.read()

    return HttpResponse(
        data,
        content_type=mimetype
    )


class FrontendTestCase(LiveServerTestCase):
    spec_files = None  # The tests themselves

    def test_frontend_test_cases(self):
        cls = self.__class__
        if not cls.spec_files:
            return

        files = [
            os.path.join(environment.get_application_root(), x)
            for x in cls.spec_files
        ]

        command = [settings.JASMINE_NODE_PATH, "--matchall"] + files

        try:
            subprocess.check_output(command)
        except subprocess.CalledProcessError as e:
            self.fail(e.output)


@override_settings(ROOT_URLCONF=__name__)
class TemplatedFrontendTestCase(LiveServerTestCase):
    """
        Allows running isolated JS unit tests with Jasmine by specifying
        spec files, source files and optionally a template. If there are any test
        failures the output from Jasmine will be echoed to stdout and the test
        will be classed as a failure.

        All paths are relative to the root of the project. The project URLs are not
        accessible! This is for isolated JS tests, if you need to run functional tests
        see JavascriptTestCase
    """

    source_files = None  # Files to test
    spec_files = None  # The tests themselves
    template_path = None
    timeout = 1 # How long to wait for tests to finish

    def test_frontend_test_cases(self):
        global urlpatterns
        cls = self.__class__

        if not cls.spec_files:
            return

        driver = None
        try:
            urlpatterns[:] = [
                url("^$", _view_factory(cls.source_files, cls.spec_files, cls.template_path)),
                url("^(?P<path>.*)", _serve)
            ]

            # Connect to existing instance
            driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME
            )

            driver.get(self.live_server_url)
            time.sleep(cls.timeout)

            stacktraces = driver.find_elements_by_xpath(
                '//div[@class="jasmine-failures"]/div/div[@class="jasmine-messages"]/div[@class="jasmine-stack-trace"]'
            )

            if stacktraces:
                descriptions = "\n\n".join([x.text for x in stacktraces])
                self.fail(descriptions)

        finally:
            urlpatterns[:] = []
            if driver:
                driver.quit()


def nose_ignore(func):
    # Intentionally don't use wraps, Nose uses __name__ to determine if it's a test
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


class JavascriptTestCase(LiveServerTestCase):
    """
        A subclass of LiveServerTestCase with an additional
        method: run_javascript_tests which takes the path
        to a JS file which runs test and returns the number of failures.

        If the number of failures > 0 then the Django test will fail
        and the captured output from stdout will be echoed to the console.

        You can access the running chromedriver service on port 4444
    """
    @nose_ignore
    def run_javascript_tests(self, javascript_files):
        files = [
            os.path.join(environment.get_application_root(), x)
            for x in javascript_files
        ]

        command = [settings.JASMINE_NODE_PATH, "--matchall"] + files

        try:
            subprocess.check_output(command)
        except subprocess.CalledProcessErro as e:
            self.fail(e.output)
