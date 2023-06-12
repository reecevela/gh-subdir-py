import requests
import os

class gh_subdir:
    def __init__(self, config):
        self.owner = config["owner"]
        self.repo = config["repo"]
        self.create_subfolder = config["create_subfolder"] if "create_subfolder" in config else True

    def download(self, base_path, path=''):
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

            if self.create_subfolder:
                os.makedirs(base_path + '/' + relative_path, exist_ok=True)
                with open(base_path + '/' + relative_path + '/' + url.split('/')[-1], write_mode) as file:
                    file.write(content)
            else:
                with open(url.split('/')[-1], write_mode) as file:
                    file.write(content)

#Example Usage:
#
#from gh_subdir import gh_subdir
#
#ghs_config = {
#    "owner": "owner",
#    "repo": "repo"
#}
#
#ghs = gh_subdir(ghs_config)
#
#ghs.download("subfolder_name")