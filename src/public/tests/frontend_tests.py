from core.test import FrontendTestCase, JavascriptTestCase, TemplatedFrontendTestCase


class SampleTestCase(TemplatedFrontendTestCase):
    spec_files = [
        "public/static/specs/example.js"
    ]


class HeadlessTestCase(FrontendTestCase):
    spec_files = [
        "public/static/specs/example.js"
    ]


class FunctionalTestCase(JavascriptTestCase):
    def test_basic_usage(self):
        self.run_javascript_tests("public/static/specs/example.js")
