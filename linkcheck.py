import mechanize
import cookielib
import argparse
from urllib2 import HTTPError


def checkRedirects(url):
    browser = mechanize.Browser()
    cookiejar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookiejar)
    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2"
    browser.addheaders = [('User-Agent', useragent)]

    try:
        response = browser.open(url)
        print url
        print response.geturl()
        print response.code
    except HTTPError, e:
        print "Error Code: %s" % e
        print "Error url %s" % url


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to check redirects")
    parser.add_argument("--file", action='store',
        dest='file', help="enter filename", type=str)
    results = parser.parse_args()
    if(type(results.file) == str):
        openFile = open(results.file, "r")
        urls = openFile.readlines()
        openFile.close()
        for url in urls:
            httpurl = "http://" + url
            httpsurl = "https://" + url
            checkRedirects(httpurl)
            checkRedirects(httpsurl)
    else:
        print "Please enter a valid filename"
