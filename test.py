#!/usr/bin/python
# -*- coding=UTF8 -*-
import xml.dom.minidom
from xml.dom.minidom import parse
#http://www.runoob.com/python/python-xml.html
DOMTree =parse('./http_sampler.xml')
collection=DOMTree.documentElement
if collection.hasAttribute('version'):
    print collection.getAttribute('version')
