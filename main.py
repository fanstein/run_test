import ConfigParser

cf = ConfigParser.ConfigParser()


cf.read("runtime_setting.ini")
print cf.get("script", "url")

