#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
带参数的请求：
1. URL Parameters:
    params: request.get(url, params={'key1':'values1'})
2. 表单参数提交
    requests.post(url, data={'key1':'value1','key2':'value2'})
3. json参数提交
    requests.post(url, json={'key1':'value1','key2':'value2'})
"""

import json
import requests
from requests import exceptions

URL = 'https://api.github.com'


def build_uri(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    # response = requests.get(build_uri('users/yuanyaru'))
    response = requests.get(build_uri('user/emails'), auth=('yuanyaru', '930313yyr'))
    print(better_print(response.text))


def params_request():
    response = requests.get(build_uri('users'), params={'since': '11'})
    print better_print(response.text)
    print response.request.headers
    print response.url


def json_request():
    # response = requests.patch(build_uri('user'), auth=('yuanyaru', '930313yyr'), json={'name': 'GM-yyr'})
    response = requests.post(build_uri('user/emails'), auth=('yuanyaru', '930313yyr'), json=['helloworld@github.com'])
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code


def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print response.text
        print response.status_code


if __name__ == '__main__':
    # request_method()
    # params_request()
    # json_request()
    timeout_request()