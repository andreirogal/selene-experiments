# -*- coding: utf-8 -*-
from selene import by, be, have
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser


def test_google(browser_config):
    browser.open("/")
    s(by.name("q")).should(be.blank) \
        .type("selenium").press_enter()
    ss(".srg .g").should(have.size_greater_than(0)) \
        .first.should(have.text("Selenium automates browsers"))


def test_google_passed(browser_config):
    browser.open("/")
    s(by.name("q")).should(be.blank) \
        .type("selenium").press_enter()
    ss(".srg .g").should(have.size_greater_than(0)) \
        .first.should(have.text("The Selenium project is a member of Software "
                                "Freedom Conservancy"))
