import requests
import os

class gh_subdir:
    def __init__(self, config):
        self.owner = config["owner"]
        self.repo = config["repo"]
        self.create_subfolder = config["create_subfolder"] if "create_subfolder" in config else True

    def download(self, path):
        base_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents"
        download_urls = []
        dir_urls = []

        response = requests.get(f"{base_url}/{path}") 
        for item in response.json():
            if item["type"] == "file":
                download_urls.append(item["download_url"])
            elif item["type"] == "dir":
                dir_urls.append(item["url"])
        
        while len(dir_urls) > 0:
            response = requests.get(dir_urls.pop())
            for item in response.json():
                if item["type"] == "file":
                    download_urls.append(item["download_url"])
                elif item["type"] == "dir":
                    dir_urls.append(item["url"])
        
        for url in download_urls:
            response = requests.get(url)

            if self.create_subfolder:
                if not os.path.exists(path):
                    os.makedirs(path)

                with open(f"{path}/{url.split('/')[-1]}", "w") as file:
                    file.write(response.text) 

            else:
                with open(url.split('/')[-1], "w") as file:
                    file.write(response.text)     

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
#ghs.download("backend_subfolder")
