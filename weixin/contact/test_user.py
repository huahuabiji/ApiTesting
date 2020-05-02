#! /usr/bin/env python
# coding=utf-8
from weixin.contact.token import Weixin
import requests
import time,logging,pystache


class TestUser:
    depart_id=1
    @classmethod
    def setup_clazz(cls):
        # todo:create depart
        pass

# 创建联系人
    def test_create(self):
        uid="huakai"+str(int(time.time()))
        data={
            "userid": uid,
            "name": uid,
            "department": [self.depart_id],
            "email": uid+"@testerhome.com"

        }
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                      params={"access_token":Weixin.get_token()},
                      json=data
                      ).json()
        logging.debug(r)
        assert r["errcode"]==0


# 获取部门成员
    def test_list(self):
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
                     params={"access_token":Weixin.get_token(),
                             "department_id":1,
                             "fetch_child":0}
                     ).json()
        logging.debug(r)

# 测试模板,has的值是false不会执行为true会执行中间内容，若是list则打印长度的次数
    def test_create_by_template(self):
        #  print(pystache.render("hello {{name}} {{#has}} world {{value}} {{/has}}",
        #                       {"name": "xiaohua",
        #                        "has": [ {"value":1},{"value":2},{"value":3} ],
        #                         "value":"good"}))
        uid="huakai_"+str(int(time.time()))
        # mobile=str(12)+str(time.time()).replace(".","")[0:9]
        data=str(self.get_user({"name":uid,
                            "title":"主管",
                            "email":"1215@qq.com"
                            # "mobile":mobile
                        }))
        data=data.encode("UTF-8")
        r=requests.post("https://qyapi.weixin.qq.com/cgi-bin/user/create",
                        params={"access_token":Weixin.get_token()},
                        data=data,
                        headers={"content-type":"application/json;charset=UTF-8"}
                       ).json()
        logging.debug(r)
        assert r["errcode"]==0


# 实例模板化方法
    def get_user(self, dict):
        """
        :param kwargs:
        :return:
        """
        template="".join(open("user_create.json").readlines())
        logging.debug(template)
        return pystache.render(template,dict)

# 简单模板化打印
    def test_get_user(self):
        logging.debug(self.get_user({"name":"xiaohua",
                                     "title":"校长",
                                     "email":"12@qq.com"}))

