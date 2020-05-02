#! /usr/bin/env python
# coding=utf-8

from unittest import TestCase
from weixin.contact.token import *

class TestWeixin(TestCase):
    def test_get_token(self):
        print(Weixin.get_token())
        assert Weixin.get_token() != ""




