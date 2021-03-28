# -*- coding: utf-8 -*-

import logging
import time

import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True, scope='session')
def session_scope():
    start = time.time()
    yield
    logging.info(f'session duration : {time.time() - start} seconds')


@pytest.fixture(scope="function")
def selene_config():
    start = time.time()
    logging.info(f'start config browser : {time.time() - start} seconds')
    browser.config.browser_name = "chrome"
    browser.config.base_url = "https://google.com"
    browser.config.timeout = 2
    browser.config.reports_folder = "selene_reports"
    logging.info(f'browser config duration: {time.time() - start} seconds')
    yield
    browser.quit()
    logging.info(f'test duration : {time.time() - start} seconds')


@pytest.fixture(scope='function')
def native_selenium():
    start = time.time()
    logging.info(f'start {start}')
    logging.info(f'before start browser: {time.time() - start} seconds')
    browser = webdriver.Chrome(ChromeDriverManager().install())
    logging.info(f'browser start duration: {time.time() - start} seconds')
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    logging.info(f'test duration : {time.time() - start} seconds')
