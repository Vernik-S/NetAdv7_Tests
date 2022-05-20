import requests
import os
from pprint import pprint


class YaCreator:
    host = "https://cloud-api.yandex.net:443"

    def __init__(self, token: str):
        self.token = token
        self.set_headers()

    def set_headers(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_href(self, yadisk_file_path):
        method = "/v1/disk/resources/upload"
        href = self.host + method
        file_name = os.path.basename(yadisk_file_path)
        params = {"path": file_name, "overwrite": "true"}
        response = requests.get(url=href, headers=self.headers, params=params)
        res = response.json()
        # print(res)
        self.upload_href = res["href"]

    def upload(self, file_path: str):
        self.get_href(file_path)
        # cur_path = os.getcwd()
        # file_path = os.path.join(cur_path, file_path)
        # print(file_path)
        # with open(file_path, "rb") as upload_file:
        # aaa = upload_file.read()
        #     print(aaa)
        response = requests.put(url=self.upload_href, data=open(file_path, 'rb'))
        print(response.status_code)

    def create_dir(self, dir_name):
        method = "/v1/disk/resources"
        href = self.host + method
        params = {"path": dir_name, "overwrite": "true"}
        response = requests.put(url=href, headers=self.headers, params=params)
        #pprint(response.json())
        return response.status_code

    def get_dir_list(self):
        method = "/v1/disk/resources"
        href = self.host + method
        params = {"path": "disk:/"}
        response = requests.get(url=href, headers=self.headers, params=params)
        res = response.json()
        #pprint(response.json())
        dirs_paths = []
        for item in res['_embedded']['items']:
            #print (item)
            if item['type'] == 'dir':
                dirs_paths.append(item['path'])
        return dirs_paths



    def del_dir(self, dir_name):
        method = "/v1/disk/resources"
        href = self.host + method
        params = {"path": dir_name, }
        response = requests.delete(url=href, headers=self.headers, params=params)
        # pprint(response.json())
        return response.status_code



if __name__ == '__main__':
    with open("yandex_token.txt") as token_file:
        token = token_file.read()
    # token = ""

    yandex = YaCreator(token)
    #yandex.upload("files\\test2.txt")

    print(yandex.create_dir(""))
    print(yandex.create_dir("Net_test"))
    print(yandex.get_dir_list())
    print(yandex.del_dir("Net_test"))
    print(yandex.get_dir_list())

