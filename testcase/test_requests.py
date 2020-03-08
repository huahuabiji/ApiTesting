#! /usr/bin/env python
# coding=utf-8

# 导入依赖
import requests
import logging
import pytest
import json

# 导入库做封装
class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    url = "https://testerhome.com/api/v3/topics.json?limit=2"
    def test_get(self):
        # r=requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        # 定义r为请求的响应内容
        r=requests.get(self.url)
        logging.info(r)
        # 获取响应内容的text部分
        logging.info(r.text)
        # json 格式输出reponse
        logging.info(json.dumps(r.json(), indent=2))


    # get常用params
    # params 参数是拼接在了url后边，使用data 参数就会在请求体单独里边，请求头里边无content_type

    # post常用参数
    # post 请求，url参数、params请求体参数、proxies代理参数、verity不需要证书验证参数
    # data 参数是请求体 2&content string,请求头content_type是text
    # json 参数是请求体 {"a":1, "b":"string content”}，请求头content_type是json
    # header 可添加自定义的参数，在请求的headers里边展示
    def test_post(self):
        r=requests.get(self.url,
                        params={"a":1, "b":"string corntent"},
                        # data={"a":1, "b":"string content"},
                        # json={"a":1, "b":"string content"},
                        headers={"a":"1", "b":"2"},
                        # proxies={"http":"127.0.0.1:8888"},
                        # verify=False
                        )
        logging.info(r)
        # 获取响应内容的text部分
        logging.info(r.text)
        # json 格式输出reponse
        logging.info(json.dumps(r.json(), indent=2))










