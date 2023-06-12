import requests
import os

class gh_subdir:
    def __init__(self, config):
        self.owner = config["owner"]
        self.repo = config["repo"]
        self.encoding = config["encoding"] if "encoding" in config else "utf-8"
        self.create_subfolder = config["create_subfolder"] if "create_subfolder" in config else True

    def install(self, base_path, path=''):
        base_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents"
        download_urls = []
        dir_urls = [(base_url + '/' + base_path, path)]

        while len(dir_urls) > 0:
            url, relative_path = dir_urls.pop()
            response = requests.get(url)
            for item in response.json():
                print(f"Downloading {item['name']}, type: {item['type']}")
                if item["type"] == "file":
                    download_urls.append((item["download_url"], relative_path))
                elif item["type"] == "dir":
                    new_path = relative_path + '/' + item["name"] if relative_path else item["name"]
                    dir_urls.append((item["url"], new_path))

        for url, relative_path in download_urls:
            print(f"Downloading {url}")
            
            response = requests.get(url)
            if response.headers['Content-Type'].startswith('text'):
                write_mode = 'w'
                content = response.text
            else:
                write_mode = 'wb'
                content = response.content

            try:
                if self.create_subfolder:
                    os.makedirs(base_path + '/' + relative_path, exist_ok=True)
                    with open(base_path + '/' + relative_path + '/' + url.split('/')[-1], write_mode, encoding=self.encoding) as file:
                        file.write(content)
                else:
                    with open(url.split('/')[-1], write_mode, encoding=self.encoding) as file:
                        file.write(content)
            except Exception as e:
                print(f"Failed to download {url}: {e}")
