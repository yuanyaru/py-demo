# -*- coding:utf-8 -*-
import requests


# 下载图片，文件
def download_image():
    url = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=517297135,2728824910&fm=26&gp=0.jpg"
    response = requests.get(url, stream=True)
    # print response.status_code, response.reason
    # print response.headers
    # print response.content
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    url = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=517297135,2728824910&fm=26&gp=0.jpg"
    from contextlib import closing
    with closing(requests.get(url, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == '__main__':
    # download_image()
    download_image_improved()