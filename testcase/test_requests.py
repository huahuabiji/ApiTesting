#! /usr/bin/env python
# coding=utf-8

import requests
import logging
import pytest
import json

# 导入库做封装
class TestRequests(object):
    logging.basicConfig(level=logging.INFO)
    def test_get(self):
        r=requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        logging.info(r)
        logging.info(r.text)
        logging.info(json.dumps(r.json(), indent=2))



