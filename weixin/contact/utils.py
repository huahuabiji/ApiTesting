#! /usr/bin/env python
# coding=utf-8

import logging
import pystache

# 实例模板化方法
class Utils:
    @classmethod
    def parse(self,template_path,dict):
        """
        :param kwargs:
        :return:
        """
        template="".join(open(template_path).readlines())
        logging.debug(template)
        return pystache.render(template,dict)