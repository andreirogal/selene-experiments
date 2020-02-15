# -*- coding: utf-8 -*-

from selene import by, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_google_one(selene_config):
    browser.open("/")
    s(by.name("q")).should(be.blank) \
        .type("selenium").press_enter()
    ss(".srg .g").should(have.size_greater_than(0)) \
        .first.should(have.text("Selenium automates browsers"))


def test_google_two(selene_config):
    browser.open("/")
    s(by.name("q")).should(be.blank) \
        .type("selenium").press_enter()
    ss(".srg .g").should(have.size_greater_than(0)) \
        .first.should(have.text("The Selenium project is a member of Software "
                                "Freedom Conservancy"))
