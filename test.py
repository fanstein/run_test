#!/usr/bin/python
# -*- coding=UTF8 -*-
from xml.etree.ElementTree import Element

import xml_parser

# 1. 读取xml文件
tree = xml_parser.read_xml("./test.xml")

# 5. 修改节点文本
# 定位节点
text_nodes = xml_parser.get_node_by_keyvalue(xml_parser.find_nodes(tree, "processers/services/service/chain"), {"sequency": "chain3"})
xml_parser.change_node_text(text_nodes, "new text")

# 6. 输出到结果文件
xml_parser.write_xml(tree, "out.xml")
