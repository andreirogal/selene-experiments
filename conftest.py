# -*- coding: utf-8 -*-

import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope="function")
def selene_config():
    browser.config.browser_name = "chrome"
    browser.config.base_url = "https://google.com"
    browser.config.timeout = 2
    browser.config.reports_folder = "selene_reports"
    yield
    browser.quit()


@pytest.fixture(scope='function')
def native_selenium():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
