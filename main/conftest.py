import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = 'chrome'
    # browser.config.base_url = 'https://hh.ru'
    # browser.config.timeout = 5




@pytest.fixture(scope='function', autouse=True)
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

