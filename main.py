from bs4 import BeautifulSoup
import requests
import urllib.request
import re

# Scraping some mp3

# Get a single url
url = 'http://www.kazaniaksiedzapiotra.pl/page/2/'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, features="html.parser")

tags = soup('a')

links = []

with requests.Session() as req:
    for tag in tags:
        href = tag.get('href')

        # print(f'Downloading file: "{href}"')
        # download = req.get(href)
        if re.match('.*mp3$', str(href)):
            name = href.split('.mp3')[0].split('/')[-1]
            print(f'Downloading file: "{name}"')
            download = req.get(href)
            if download.status_code == 200:
                with open(name + '.mp3', 'wb') as f:
                    f.write(download.content)
            else:
                print(f"Download Failed For File {name}")


