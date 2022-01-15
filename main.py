import os

from download_mp3_files import download_mp3_files
from find_mp3_urls import find_mp3_urls

base_url = 'http://www.kazaniaksiedzapiotra.pl/page/'
download_dir = 'downloads'

if __name__ == '__main__':
    first_page = input('First page: ')
    last_page = input('Last page: ')

    urls_to_scrape = []

    for i in range(int(first_page), int(last_page) + 1):
        urls_to_scrape.append(base_url + str(i))

    mp3_urls = []
    for url in urls_to_scrape:
        mp3_urls.extend(find_mp3_urls(url))

    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    download_mp3_files(mp3_urls, download_dir)
