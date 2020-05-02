#! /usr/bin/env python
# coding=utf-8

# 导入依赖
import requests
import logging
import pytest
import json
from jsonschema import validate
from hamcrest import *

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
    # headers 可添加自定义的参数，在请求的headers里边展示
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


    def test_cookies(self):
        r=requests.get(self.url, cookies={"a":"1", "b":"string corntent"})
        logging.info(r.text)


    # 带有cookies的get请求
    def test_xueqiu_quote(self):
        url="https://xueqiu.com/v5/stock/portfolio/stock/list.json"
        r=requests.get(self.url,
                       params={"category":"1"},
                       headers={"user_Agent":"xueqiu"},
                       cookies={"u":"3446260779","xq_a_token":"5806a70c6bc5d5fb2b00978aeb1895532fffe502"},
                       # proxies={"http":"127.0.0.1:8888"},
                       # verity=False
                    )
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))
       # 断言 assert r.json()["data"]["category"] == 2


    def test_fee_search(self):
        url = "https://tx.tianxiao100.com/api/course/fee/page"
        r = requests.post(self.url,
                          json={"keyword": "12"},
                          headers={"content_type":"application/json;charset=UTF-8",
                                   "curcampusid": "75286",
                                   "curcampusnumber": "665196029",
                                   "Auth-Token":"M34lcnVqTGclPTU4OTwvJWZkcHN4dkxnJT06ODU7OS8ldndkaWlMZyU9NDYvJXZ3eGdocXhNaCY-cnlwcDAmZ3B5aU1oJj5yeXBwMCZxc2ZtcGkmPnJ5cHAwJnl3aXZNaCY-cnlwcDEne254bnl0d05pJz9zenFxMSd0dWpzTmknP3N6cXExJ2h5Jz82Oj06Pjs7NjU9PDs2MSh5Z3J6KEAoOT5dZzuAeXwoMih8a3h5b3V0KEA2MihrdHwoQCgoMihpZ3lpZ2prT2ooQDeE",
                                   "userNumber":"665196029",
                                   "Hm_lpvt_ac04e67886d6a73a7a36e6aad0b214e8":"1585966116"
                                   }
                          )
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(),indent=2))
       # assert r.json()["data"]["records"][0]["name"]=="123"


    def test_hamcrest(self):
        assert_that(0.1 * 0.1, close_to(0.01, 0.0001))
        assert_that(
            ["a", "b", "c"],
            all_of(
                has_items("c","d"),
                has_items("c","a")
            )
        )


    def test_schema(self):
        schema = {
            "type" : "object",
            "properties" : {
                "price" : {"type" : "number"},
                "name" : {"type" : "string"}
            },

        }
        validate(instance={"name" : "eggs", "price" : "33.99"}, schema=schema)









