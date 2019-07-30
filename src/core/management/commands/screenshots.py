from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.conf import settings
from django.core.management.base import BaseCommand

import os

SCREEN_SIZES = {
    'laptop': {
        'size': (1440, 900),
        'focused_element': 'dmb-dimension-tabs'
    },
    'tablet': {
        'size': (556, 796),
        'focused_element': 'dmb-progress-circle'
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


def take_screenshot(driver, focused_element, path):
    driver.execute_script("arguments[0].scrollIntoView();", focused_element)
    # Arbitrary padding
    driver.execute_script("window.scrollBy(0, -10);")
    # Hide any debug or unwanted elements
    for selector in HIDDEN_SELECTORS:
        driver.execute_script(
            "if (document.querySelector('{0}')) document.querySelector('{0}').style.display = 'none'"
            .format(selector)
        )
    # Arbitrary timeout of scrollbar
    driver.save_screenshot(path)


def take_screenshots(driver, path, retina=False):
    # Hide the scrollbar
    driver.execute_script(
        "document.body.style.overflowY = 'hidden'"
    )
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
        if retina:
            take_screenshot(driver, element, path + '/{}@2x.png'.format(screen_name))
        else:
            take_screenshot(driver, element, path + '/{}.png'.format(screen_name))


def take_tenant_screenshots(driver, retina=False):
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
                take_screenshots(driver, path, retina)
        else:
            driver.get('http://localhost:8000/{}/reports/{}'
                       .format(tenant['slug'], tenant['screenshot_report_id']))
            path = BASE_PATH + "/{}/home".format(tenant_name)
            take_screenshots(driver, path, retina)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Take 1x screenshots
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--force-device-scale-factor=1")
        driver = webdriver.Chrome(options=chrome_options)
        take_tenant_screenshots(driver)
        driver.close()
        # Take 2x screenshots
        retina_options = webdriver.ChromeOptions()
        retina_options.add_argument("--force-device-scale-factor=2")
        retina_driver = webdriver.Chrome(options=retina_options)
        take_tenant_screenshots(retina_driver, retina=True)
        retina_driver.close()
