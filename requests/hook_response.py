# -*- coding:utf-8 -*-

import requests


# 回调函数
def get_key_info(response, *args, **kwargs):
    print response.headers['Content-Type']


# 主函数
def main():
    # requests.get("https://www.baidu.com", hooks=dict(response=get_key_info))
    requests.get("https://api.github.com", hooks=dict(response=get_key_info))


if __name__ == '__main__':
    main()