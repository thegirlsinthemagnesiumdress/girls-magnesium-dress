#!/usr/bin/env python
import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
APPENGINE_DIR = os.path.join(THIS_DIR, "third_party", "google_appengine")
DEVELOPMENT_DIR = os.path.join(THIS_DIR, "third_party", "local", "sitepackages")

sys.path[0:0] = [
    os.path.join(THIS_DIR, 'src'),
    APPENGINE_DIR,
    DEVELOPMENT_DIR
]

from core.boot import fix_path
fix_path()

if __name__ == "__main__":
    # Make sure that if we are deploying and we don't specify any settings
    # that we use the live ones
    if "deploy" in sys.argv and "--settings" not in sys.argv:
        print("NOTE: Using core.settings.live as we are deploying")
        os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings.live"
    elif "test" in sys.argv:
        print("NOTE: Using core.settings.local as we are testing")
        os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings.local"

    if "test" in sys.argv:
        from djangae.core.management import test_execute_from_command_line
        test_execute_from_command_line(sys.argv)
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
        from djangae.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
