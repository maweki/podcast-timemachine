import time
from xml.dom.minidom import parse
from dateutil.parser import parse as parsedate
from datetime import timedelta, datetime, timezone

def download(url):
    import urllib.request
    return urllib.request.urlopen(url)

def delayFeed(url, delay):
    dom = parse(download(url))
    fix(dom, delay)
    return dom.toxml()

def fix(root, delay):
    delta = timedelta(days=delay)
    if root.nodeType == root.ELEMENT_NODE:
        if root.tagName == "title":
            titlenode = root.childNodes[0]
            titlenode.replaceWholeText(titlenode.nodeValue + ' (DELAYED ' + str(delay) + ' days)')
        if root.tagName == "pubDate":
            datenode = root.childNodes[0]
            d = parsedate(datenode.nodeValue) + delta
            if d > datetime.now(timezone.utc):
                itemnode = datenode.parentNode.parentNode
                itemnode.parentNode.removeChild(itemnode)
                pass
            else:
                datenode.replaceWholeText(str(d))
    for child in root.childNodes:
        fix(child, delay)
