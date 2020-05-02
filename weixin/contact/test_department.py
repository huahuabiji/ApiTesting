#! /usr/bin/env python
# coding=utf-8

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


    def test_create_order(self):
        data={
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1,
        }
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/department/create",
                        params={"access_token":Weixin.get_token()},
                        json=data
                      ).json()
        logging.debug(r)

    def test_get(self):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/department/list",
                     params={"access_token":Weixin.get_token()}
                       ).json()
        logging.info(json.dumps(r, indent=2))
        # logging.debug(r)
