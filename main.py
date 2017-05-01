import ConfigParser

import xml_parser

cf = ConfigParser.ConfigParser()

cf.read("runtime_setting.ini")
data = []
sections = ['script', 'scenario', 'data']
# print cf.sections()
host = cf.get('script', 'host_port')
path = cf.get('script', 'path')
method = cf.get('script', 'method')
bodydata = cf.get('script', 'bodydata')
parameter = cf.get('script', 'parameter')
print parameter

# 如果parameter为true读data节点
if parameter == 'true':
    print 11

# 把参数注入脚本
tree = xml_parser.read_xml('http_sampler.jmx')
nodes = xml_parser.find_nodes(tree, 'hashTree/hashTree/hashTree/HTTPSamplerProxy/stringProp')
path_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.path'})
host_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.path'})
port_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.path'})
method_node = xml_parser.get_node_by_keyvalue(nodes, {'name': 'HTTPSampler.path'})
