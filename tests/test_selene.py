# -*- coding: utf-8 -*-

import logging
import time

from selene import by, be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

logger = logging.getLogger(__name__)


def test_google_one(selene_config):
    start = time.time()
    logger.info(f'before start browser: {time.time() - start} seconds')
    browser.open("/")
    logger.info(f'browser start duration: {time.time() - start} seconds')
    s(by.name("q")).should(be.blank) \
        .type("selenium").press_enter()
    ss(".srg .g").should(have.size_greater_than(0)) \
        .first.should(have.text("Selenium automates browsers"))


def test_google_two(selene_config):
    start = time.time()
    logger.info(f'before start browser: {time.time() - start} seconds')
    browser.open("/")
    logger.info(f'browser start duration: {time.time() - start} seconds')
    s(by.name("q")).should(be.blank) \
        .type("selenium").press_enter()
    ss(".srg .g").should(have.size_greater_than(0)) \
        .first.should(have.text("The Selenium project is a member of Software "
                                "Freedom Conservancy"))
