#! /usr/bin/env python
# coding=utf-8
import pytest

from weixin.contact.token import *
import requests
import logging,json,datetime

class TestDepartment:
    @classmethod
    def setup_class(cls):
        print("setup_class")
        Weixin.get_token()
        print(Weixin._token)

    def setup(self):
        print("setup")

# 测试创建多层级的部门，最多15
    def test_create_depth(self):
        parentid=1
        t=str(int(datetime.datetime.now().timestamp()))
        for i in range(5):
            data={
                "name": "xiaokai"+str(parentid)+t,
                "parentid": parentid
                   }
            r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                            params={"access_token":Weixin.get_token()},
                            json=data,
                            # proxies={"http":"http://127.0.0.1:8888",
                            #          "https": "http://127.0.0.1:8888"
                            #          },
                            # verify=False
                          ).json()
            logging.info(json.dumps(r, indent=2))
            logging.debug(r)
            parentid=r["id"]
            assert r["errcode"]==0

    # def test_create_name(self):
    #     data={
    #         "name": "hukai_03",
    #         "parentid": 1
    #            }
    #     r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
    #                     params={"access_token":Weixin.get_token()},
    #                     json=data
    #                   ).json()
    #     logging.info(json.dumps(r, indent=2))
    #     logging.debug(r)

# name字符测试 参数化
    @pytest.mark.parametrize("name",{
        "东京动漫研究所",
        "도쿄 애니메이션 연구소",
        "東京アニメ研究所",
        "معهد طوكيو أنمي للأبحاث",
        "Токио аниме изследователски институт"
    })
    def test_create_order(self,name):
        data={
                "name": name,
                "parentid": 1,
                "order": 1,
        }
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                        params={"access_token":Weixin.get_token()},
                        json=data
                      ).json()
        logging.debug(r)
        assert r["errcode"]==0


    def test_get(self):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token":Weixin.get_token()}
                       ).json()
        logging.info(json.dumps(r, indent=2))
        # logging.debug(r)
