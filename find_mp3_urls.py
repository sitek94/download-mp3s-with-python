from bs4 import BeautifulSoup
import urllib.request
import re


def find_mp3_urls(url):
    """
    Go to a given url and find all the urls ending with ".mp3"
    """
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    mp3_urls = []

    tags = soup('a')
    for tag in tags:
        href = tag.get('href')
        if re.match('.*mp3$', str(href)):
            mp3_urls.append(href)

    return mp3_urls
