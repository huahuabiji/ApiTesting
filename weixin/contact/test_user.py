#! /usr/bin/env python
# coding=utf-8
from weixin.contact.token import Weixin
import requests
import time,logging,pystache
from weixin.contact.user import User
from weixin.contact.utils import Utils


class TestUser:
    depart_id=1
    @classmethod
    def setup_class(cls):
        # todo:create depart
        cls.user=User()

# 创建联系人
    def test_create(self):
        uid="huakai"+str(int(time.time()))
        data={
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid+"@testerhome.com"

        }
        r=self.user.create(data)
        logging.debug(r)
        assert r["errcode"]==0


# 获取部门成员
    def test_list(self):
        r=self.user.list()
        logging.debug(r)

        r=self.user.list(department_id=2)
        logging.debug(r)

# 测试模板,has的值是false不会执行为true会执行中间内容，若是list则打印长度的次数
    def test_create_by_template(self):
        #  print(pystache.render("hello {{name}} {{#has}} world {{value}} {{/has}}",
        #                       {"name": "xiaohua",
        #                        "has": [ {"value":1},{"value":2},{"value":3} ],
        #                         "value":"good"}))
        uid = "huakai_"+str(int(time.time()))
        mobile = str(12)+str(time.time()).replace(".", "")[0:9]
        data = str(Utils.parse("user_create.json", {
            "name": uid,
            "title": "产品",
            "email": mobile + "@qq.com"
            }))
        data = data.encode("UTF-8")
        #r = self.user.create(data)
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                        params={"access_token": Weixin.get_token()},
                        data=data,
                        headers={"content-type":"application/json;charset=UTF-8"}
                       ).json()
        logging.debug(r)
        assert r["errcode"]==0


# 简单模板化打印
    def test_get_user(self):
        data={"name":"xiaohua",
              "title":"校长",
              "email":"12@qq.com"}
        logging.debug(Utils.parse("user_create.json",data))

