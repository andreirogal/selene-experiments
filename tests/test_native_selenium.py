# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def test_google_one(native_selenium):
    native_selenium.get("https://google.com")
    search_input = native_selenium.find_element_by_name('q')
    search_input.clear()
    search_input.click()
    search_input.send_keys('selenium')
    search_input.send_keys(Keys.RETURN)
    WebDriverWait(native_selenium, timeout=3).until(
        lambda wait: len(native_selenium.find_elements(
            *(By.CSS_SELECTOR, '.srg .g'))) > 0)
    results = native_selenium.find_elements_by_css_selector('.srg .g')
    assert 'Selenium automates browsers' in results[0].text


def test_google_two(native_selenium):
    native_selenium.get("https://google.com")
    search_input = native_selenium.find_element_by_name('q')
    search_input.clear()
    search_input.click()
    search_input.send_keys('selenium')
    search_input.send_keys(Keys.RETURN)
    WebDriverWait(native_selenium, timeout=3).until(
        lambda wait: len(native_selenium.find_elements(
            *(By.CSS_SELECTOR, '.srg .g'))) > 0)
    results = native_selenium.find_elements_by_css_selector('.srg .g')
    assert 'The Selenium project is a member of Software Freedom Conservancy' \
           in results[0].text
