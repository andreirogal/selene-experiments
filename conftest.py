# -*- coding: utf-8 -*-
import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function")
def browser_config():
    browser.config.browser_name = "chrome"
    browser.config.base_url = "https://google.com"
    browser.config.timeout = 2
    browser.config.reports_folder = "selene_reports"
    yield
    print("\nexit from browser")
    browser.quit()
