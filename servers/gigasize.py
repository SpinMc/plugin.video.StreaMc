# -*- coding: utf-8 -*-

from platformcode import logger
from core import scrapertools


def test_video_exists(page_url):
    logger.info("(page_url='%s')" % page_url)

    # Vídeo borrado: http://www.gigasize.com/get/097fadecgh7pf
    # Video erróneo: 
    data = scrapertools.cache_page(page_url)
    if '<h2 class="error">Download error</h2>' in data:
        return False,"Il video non esiste più su gigasize"
    else:
        return True, ""


def get_video_url(page_url, premium=False, user="", password="", video_password=""):
    logger.info("(page_url='%s')" % page_url)
    video_urls = []

    return video_urls
