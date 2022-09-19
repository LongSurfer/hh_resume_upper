import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from utils import attach
from dotenv import load_dotenv


DEFAULT_BROWSER_VERSION = '100.0'

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()

    @pytest.fixture(scope='function')
    def setup_browser(request):
        browser_version = request.config.getoption('--browser_version')
        browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        username = os.getenv('USERNAME')
        pswrd = os.getenv('PSWRD')

        driver = webdriver.Remote(
            command_executor=f"https://{username}:{pswrd}@selenoid.autotests.cloud/wd/hub",
            options=options)
        browser = Browser(Config(driver))
        yield browser

        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
        browser.quit()


# @pytest.fixture(scope='function', autouse=True)
# def browser_management():
#     browser.config.browser_name = 'chrome'
#     browser.config.base_url = 'https://hh.ru/'


# @pytest.fixture(scope='function', autouse=True)
# def browser_size():
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080

