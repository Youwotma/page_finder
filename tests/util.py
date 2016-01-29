import urlparse

import scrapely


def is_link(fragment):
    """True if the HtmlPage fragment is a link"""
    return (isinstance(fragment, scrapely.htmlpage.HtmlTag) and
            fragment.tag == 'a' and
            fragment.tag_type == scrapely.htmlpage.HtmlTagType.OPEN_TAG)


def _extract_all_links(page_or_url):
    """Generate all links of a page in the order they are found"""
    if not isinstance(page_or_url, scrapely.htmlpage.HtmlPage):
        page = scrapely.htmlpage.url_to_page(page_or_url)
    else:
        page = page_or_url

    for fragment in page.parsed_body:
        if is_link(fragment):
            link = fragment.attributes.get('href')
            if link:
                yield urlparse.urljoin(page.url, link)


def extract_all_links(page_or_url):
    """Return a list of unique links in the page (unoredered)"""
    return list({link for link in _extract_all_links(page_or_url)})
