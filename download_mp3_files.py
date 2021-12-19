from tqdm import tqdm
import requests

download_dir = 'output/'


def download_mp3_files(urls):
    """
    Downloads mp3 files from a url list
    """
    with requests.Session() as request:
        for url in urls:
            name = url.split('.mp3')[0].split('/')[-1]
            response = request.get(url, stream=True)

            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, colour='blue')

            if response.status_code == 200:
                with open('output/' + name + '.mp3', 'wb') as file:
                    for data in response.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)

            progress_bar.close()

            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print('Something went wrong!')
