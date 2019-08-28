from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from django.conf import settings
from core.models import Survey, SurveyResult
from django.core.management.base import BaseCommand

import os
import logging
import subprocess

DEFAULT_SCREEN_SIZES = {
    'laptop': {
        'size': (1440, 900),
        'focused_element': 'dmb-dimension-tabs'
    },
    'tablet': {
        'size': (600, 860),
        'focused_element': 'dmb-report-overall'
    },
    'mobile': {
        'size': (400, 820),
        'focused_element': 'dmb-report-overall'
    },
}

HIDDEN_SELECTORS = [
    '.dmb-dimension-tabs__sticky-nav',
    '.djdt-hidden',
    '.dmb-report-debug-toggle',
    '.dmb-header'
]

DEFAULT_LANGUAGE_CODES = [key for key, lang in settings.LANGUAGES]

DEFAULT_TENANTS = settings.TENANTS

BASE_PATH = os.path.join(settings.BASE_DIR, "static/src/img/")


def take_screenshot(driver, focused_element, path):
    """Takes an individual screenshot of a specific element and saves it to
    a specified path.

    Args:
        driver (ChromeDriver): The selenium web driver to use to take the screenshot.
        focused_element (string): Selector for the element to be focused in the screenshot.
        path (string): File path for where to save the screenshot to.
    """
    driver.execute_script("arguments[0].scrollIntoView();", focused_element)
    # Arbitrary padding
    driver.execute_script("window.scrollBy(0, -15);")
    # Hide any debug or unwanted elements
    for selector in HIDDEN_SELECTORS:
        driver.execute_script(
            "if (document.querySelector('{0}')) document.querySelector('{0}').style.display = 'none'"
            .format(selector)
        )
    # Arbitrary timeout of scrollbar
    driver.save_screenshot(path)


def take_sized_screenshots(driver, screen_sizes, path, retina=False):
    """Takes an individual screenshot for the specified screen sizes and
    saves them as the designated path.

    Args:
        driver (ChromeDriver): The selenium web driver to use to take the screenshot.
        screen_sizes ([(number, number)]): A list of screen sizes to take screenshots for different screen sizes.
        path (string): File path for where to save the screenshot to.
        retina (bool, optional): Whether the screenshots are being taken for retina to append the right
                                 file prefixes. Defaults to False.
    """
    # Hide the scrollbar
    driver.execute_script(
        "document.body.style.overflowY = 'hidden'"
    )
    if not os.path.exists(path):
        os.makedirs(path)
    for screen_name, screen in screen_sizes.items():
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
        if screen_name == 'mobile':
            # Wait until the graph data has loaded
            _ = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'dmb-progress-grid')
                )
            )
        logging.info('Taking for screen size: (%d, %d)', w, h)
        if retina:
            take_screenshot(driver, element, path + '/{}@2x.png'.format(screen_name))
        else:
            take_screenshot(driver, element, path + '/{}.png'.format(screen_name))


def take_tenant_screenshots(driver, tenants, languages, screens, retina=False):
    """Takes screenshots for all tenants on all the specified languages (if enabled) and
    screen sizes.

    Args:
        driver (ChromeDriver): The selenium web driver to use to take the screenshots.
        tenants ([Tenant]): A list of tenant objects specifying which tenant sites to screenshot.
        languages ([string]): A list of language codes to screenshot for on appropriate tenants.
        screens ([(number, number)]): A list of screen sizes to take screenshots for different screen sizes.
        retina (bool, optional): Whether the screenshots are being taken for retina to append the right
                                 file prefixes. Defaults to False.
    """
    # Loop through tenants
    for tenant_name, tenant in tenants.items():
        logging.info('Taking screenshots for %s', tenant_name)
        # Get the example report/survey for this tenant
        report_id = Survey.objects.filter(
            tenant=tenant_name,
            company_name='ACME Corp.'
        ).order_by('-created_at').first().sid
        # If tenant supports i18n then repeat for each language
        if tenant['i18n']:
            for locale in languages:
                driver.get('http://localhost:8000/{}/{}/reports/{}'
                           .format(locale, tenant['slug'], report_id))
                path = BASE_PATH + "/{}/home".format(tenant_name)
                if locale != 'en':
                    path = BASE_PATH + "/{}/{}/home".format(locale, tenant_name)
                logging.info('Taking for language: %s', locale)
                take_sized_screenshots(driver, screens, path, retina)
        else:
            driver.get('http://localhost:8000/{}/reports/{}'
                       .format(tenant['slug'], report_id))
            path = BASE_PATH + "/{}/home".format(tenant_name)
            logging.info('Taking for language: en')
            take_sized_screenshots(driver, screens, path, retina)


def take_screenshots(tenants, languages, screens, retina=False):
    """ Sets up the chrome driver and takes screenshots for all tenants on all the
    specified languages (if enabled) and screen sizes.

    Args:
        tenants ([Tenant]): A list of tenant objects specifying which tenant sites to screenshot.
        languages ([string]): A list of language codes to screenshot for on appropriate tenants.
        screens ([(number, number)]): A list of screen sizes to take screenshots for different screen sizes.
        retina (bool, optional): Whether the screenshots are being taken for retina to append the right
                                 file prefixes. Defaults to False.
    """
    # Form the options for chomre based on if we are taking retina screenshots or not.
    chrome_options = webdriver.ChromeOptions()
    if not retina:
        logging.info('<----- Taking @1x Screenshots ----->')
        chrome_options.add_argument("--force-device-scale-factor=1")
    else:
        logging.info('<----- Taking @2x Screenshots ----->')
        chrome_options.add_argument("--force-device-scale-factor=2")
    # Launch in app mode to remove navbar and point to phony url to save loading time
    chrome_options.add_argument("--app=http://localhost:8000/not-a-url")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # Wrap in try catch to discard of driver if an error occurs.
    try:
        take_tenant_screenshots(driver, tenants, languages, screens, retina)
    finally:
        logging.info("Cleaning up Selenium Chrome driver")
        driver.close()


class Command(BaseCommand):
    help = 'Takes screenshots of the reports page for all tenants and different screen sizes for landing page'

    def add_arguments(self, parser):
        parser.add_argument(
            '--tenant',
            help='Only take screenshots for a specified tenant',
            type=str
        )
        parser.add_argument(
            '--lang',
            help='Only take screenshots for a specified language (if tenant specified, ensure is i18n)',
            type=str
        )

    def handle(self, *args, **options):
        # Set list of tenants, languages, and screens to default before altering them based on flags.
        tenants = DEFAULT_TENANTS
        languages = DEFAULT_LANGUAGE_CODES
        screens = DEFAULT_SCREEN_SIZES
        # If we have a tenant passed make sure it is a valid tenant slug
        if options['tenant'] and options['tenant'] in DEFAULT_TENANTS:
            tenants = {options['tenant']: DEFAULT_TENANTS[options['tenant']]}
        elif options['tenant'] not in DEFAULT_TENANTS and options['tenant'] is not None:
            logging.error("Invalid tenant slug, aborting!")
            return
        # If we have a language passed make sure language code is valid
        # and that tentants have i18n enabled (unless lang=en)
        if options['lang'] and options['lang'] in DEFAULT_LANGUAGE_CODES:
            if options['lang'] != 'en':
                tenants = {k: v for k, v in tenants.items() if v['i18n']}
                if len(tenants) == 0:
                    logging.error("No i18n capable tenants selected, aborting!")
                    return
            languages = [options['lang']]
        elif options['lang'] not in DEFAULT_LANGUAGE_CODES and options['lang'] is not None:
            logging.error("Invalid language code, aborting!")
            return
        # Wrap in try catch to discard of any created example surveys if an error occurs.
        try:
            # Create fake results for screenshots.
            subprocess.call("./manage.py create_sample_survey", shell=True)
            # Take 1x screenshots
            take_screenshots(tenants, languages, screens)
            # Take 2x screenshots
            take_screenshots(tenants, languages, screens, retina=True)
        finally:
            logging.info("Cleaning up example surveys.")
            # Clean up example surveys
            for tenant in DEFAULT_TENANTS.keys():
                survey = Survey.objects.filter(
                    tenant=tenant,
                    company_name='ACME Corp.'
                ).order_by('-created_at').first()
                SurveyResult.objects.all().filter(survey_id=survey.sid).delete()
                survey.delete()
