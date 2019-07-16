from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.conf import settings
from django.core.management.base import BaseCommand

import time
import os

SCREEN_SIZES = {
    'laptop': {
        'size': (1024, 768),
        'focused_element': 'dmb-dimension-tabs'
    },
    'tablet': {
        'size': (768, 1024),
        'focused_element': 'dmb-report-overall'
    },
    'mobile': {
        'size': (400, 600),
        'focused_element': 'dmb-report-overall'
    },
}

HIDDEN_SELECTORS = [
    '.dmb-dimension-tabs__sticky-nav',
    '.djdt-hidden',
    '.dmb-report-debug-toggle',
    '.dmb-header'
]

LANGUAGE_CODES = [key for key, lang in settings.LANGUAGES]

BASE_PATH = os.path.join(settings.BASE_DIR, "static/src/img/")

DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)


def take_screenshot(focused_element, path):
    driver.execute_script("arguments[0].scrollIntoView();", focused_element)
    # Arbitrary padding
    driver.execute_script("window.scrollBy(0, -20);")
    # Hide any debug or unwanted elements
    for selector in HIDDEN_SELECTORS:
        driver.execute_script(
            "if (document.querySelector('{0}')) document.querySelector('{0}').style.display = 'none'"
            .format(selector)
        )
    # Arbitrary timeout of scrollbar
    time.sleep(0.5)
    driver.save_screenshot(path)


def take_screenshots(path):
    if not os.path.exists(path):
        os.makedirs(path)
    for screen_name, screen in SCREEN_SIZES.items():
        # Resize the screen to the correct size
        w, h = screen['size']
        # Execute script to get adjusted window size (due to chrome bar etc.)
        window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, w, h)
        driver.set_window_size(*window_size)
        # Wait until the angular content has loaded
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, screen['focused_element'])
            )
        )
        take_screenshot(element, path + '/{}.png'.format(screen_name))
        # Need some way to scale the image in python due to HTML/CSS breakpoints
        # driver.set_window_size(w * 2, h * 2)
        take_screenshot(element, path + '/{}@2x.png'.format(screen_name))


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Loop through tenants
        for tenant_name, tenant in settings.TENANTS.items():
            # If tenant supports i18n then repeat for each language
            if tenant['i18n']:
                for locale in LANGUAGE_CODES:
                    driver.get('http://localhost:8000/{}/{}/reports/{}'
                               .format(locale, tenant['slug'], tenant['screenshot_report_id']))
                    path = BASE_PATH + "/{}/home".format(tenant_name)
                    if locale != 'en':
                        path = BASE_PATH + "/{}/{}/home".format(locale, tenant_name)
                    take_screenshots(path)
            else:
                driver.get('http://localhost:8000/{}/reports/{}'
                           .format(tenant['slug'], tenant['screenshot_report_id']))
                path = BASE_PATH + "/{}/home".format(tenant_name)
                take_screenshots(path)
        # Exit the chrome driver
        driver.close()
