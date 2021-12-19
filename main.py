from download_mp3_files import download_mp3_files
from find_mp3_urls import find_mp3_urls

url = 'http://www.kazaniaksiedzapiotra.pl/page/2/'

if __name__ == '__main__':
    urls = find_mp3_urls(url)
    download_mp3_files(urls)
