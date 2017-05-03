#!/usr/bin/python
# -*- coding=UTF8 -*-
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("runtime_setting.ini")

result_path = cf.get('scenario', 'result_path')
print result_path

