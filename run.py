#!/usr/bin/python  
# -*- coding=utf-8 -*-
import ConfigParser
import sched
import sys
import time
import os

import xml_parser
from script import script_mader

cf = ConfigParser.ConfigParser()
cf.read("runtime_setting.ini")

def my_time():
    str_time = time.strftime('_%H-%M-%S', time.localtime(time.time()))
    return str_time


def run_jmeter(jscript, jlog, jpath, jthread):
    os.chdir(jpath)
    if os.path.exists("res"):
        pass
    else:
        os.mkdir("res")
    # os.system("jmeter -n -t " + jscript + " -l " + jlog + " -e -o res/" + jlog + " -Jthread=" + jthread)
    os.system("jmeter -n -t " + jscript + " -l " + jlog + " -e -o res/" + jlog + " -Jthread=" + jthread)


if __name__ == "__main__":
    jmx = (cf.get('scenario','result_path')+'out.xml').decode('utf8')
    threads = cf.get('scenario', 'users')
    thread= threads.split(',')
    log = sys.argv[2] + "_" + sys.argv[5] + "u" + my_time()
    run_time = sys.argv[4]
    thread = sys.argv[5]
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(float(run_time), 0, run_jmeter, (jmx, log, path, thread))
    print '测试开始,当前时间:', time.time()
    print schedule.queue[0]
    schedule.run()
    os.remove(log)
