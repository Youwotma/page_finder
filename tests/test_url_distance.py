# -*- coding: utf-8 -*-

from page_finder.url_distance import url_distance
from page_finder import number_preprocessor, dont_preprocess


def test_url_distance():
    assert(url_distance(dont_preprocess,
        'http://foo.bar.com/%65/foo?bar&foo#',
        'https://foo.bar.com/e/foo?foo&bar' ) == 0)

    assert(url_distance(number_preprocessor,
        'http://foo.bar.com/%65/456/foo?bar&foo#',
        'https://foo.bar.com/e/123/foo?foo&bar' ) == 0)

    assert(url_distance(number_preprocessor,
        'http://foo.bar.com/products/home/456',
        'http://foo.bar.com/products/garden/123' ) == 1)

    assert(url_distance(dont_preprocess,
        'http://foo.bar.com/?bar=1&foo=1',
        'http://foo.bar.com/?foo=1&bar=2' ) == 1)

    assert(url_distance(dont_preprocess,
        'http://foo.bar.com/ñáร์',
        'http://foo.bar.com/aaa' ) == 1)
