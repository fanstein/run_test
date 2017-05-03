#!/usr/bin/python
# -*- coding=utf-8 -*-

import ConfigParser

import xml_parser


def script_mader():
    cf = ConfigParser.ConfigParser()

    cf.read("runtime_setting.ini")
    sections = ['script', 'scenario', 'data']
    host_port = cf.get('script', 'host_port')
    path = cf.get('script', 'path')
    method = cf.get('script', 'method')
    bodydata = cf.get('script', 'bodydata')
    parameter = cf.get('script', 'parameter')
    Content_Type = cf.get('script', 'Content-Type')
    result_path = cf.get('scenario', 'result_path')
    # print parameter, host_port, bodydata

    tree = xml_parser.read_xml('http_sampler.jmx')
    # 如果parameter为true读data节点
    if parameter == 'true':
        text_nodes = xml_parser.get_node_by_keyvalue(
            xml_parser.find_nodes(tree, "hashTree/hashTree/hashTree/CSVDataSet"),
            {"name": "Argument.value"})
        xml_parser.change_node_properties(text_nodes, {"enable": "true"})

    # 添加heads
    if Content_Type:
        head_node = xml_parser.find_nodes(tree, 'hashTree/hashTree/hashTree/HeaderManager')
        xml_parser.change_node_properties(head_node, {"enable": "true"})
        header_nodes = xml_parser.get_node_by_keyvalue(
            xml_parser.find_nodes(tree,
                                  "hashTree/hashTree/hashTree/HeaderManager/collectionProp/elementProp/stringProp"),
            {"name": "Header.value"})
        xml_parser.change_node_text(header_nodes, Content_Type)

    # 把参数注入脚本
    nodes = xml_parser.find_nodes(tree, 'hashTree/hashTree/hashTree/HTTPSamplerProxy/stringProp')
    path_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.path'})
    host_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.domain'})
    port_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.port'})
    method_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.method'})
    xml_parser.change_node_text(path_node, path)
    xml_parser.change_node_text(host_node, host_port)
    xml_parser.change_node_text(method_node, method)
    if ':' in host_port:
        port = host_port.split(':')[1]
        xml_parser.change_node_text(port_node, port)

    text_nodes = xml_parser.get_node_by_keyvalue(
        xml_parser.find_nodes(tree,
                              "hashTree/hashTree/hashTree/HTTPSamplerProxy/elementProp/collectionProp/elementProp/stringProp"),
        {"name": "Argument.value"})
    xml_parser.change_node_text(text_nodes, bodydata)
    xml_parser.write_xml(tree, (result_path+'out.jmx').decode('utf8'))
    print 'script have create!'

