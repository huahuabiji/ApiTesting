#! usr/bin/env python
# coding=utf-8

import requests
from weixin.contact.token import Weixin

class User:
    def create(self,dict=None,data=None):
        return requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                             params={"access_token": Weixin.get_token()},
                             json=dict,
                             data=data,
                             headers={"content-type": "application/json;charset=UTF-8"}
                             ).json()

    def list(self,department_id=1,fetch_child=0,**kwargs):
        return requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                            params={"access_token":Weixin.get_token(),
                                    "department_id":department_id,
                                    "fetch_child":fetch_child}
                            ).json()

