import requests


download_dir = 'output/'


def download_mp3_files(urls):
    """
    Downloads mp3 files from a url list
    """
    with requests.Session() as req:
        for url in urls:
            name = url.split('.mp3')[0].split('/')[-1]
            print(f'Downloading file: "{name}"')
            download = req.get(url)
            if download.status_code == 200:
                with open('output/' + name + '.mp3', 'wb') as f:
                    f.write(download.content)
            else:
                print(f"Download Failed For File {name}")
