#!/usr/bin/python  
# -*- coding=utf-8 -*-
import sched
import sys
import time
import os


def my_time():
    str_time = time.strftime('_%H-%M-%S', time.localtime(time.time()))
    return str_time


def run_jmeter(jscript, jlog, jpath, jthread):
    os.chdir(jpath)
    if os.path.exists("res"):
        pass
    else:
        os.mkdir("res")
    os.system("jmeter -n -t " + jscript + " -l " + jlog + " -e -o res/" + jlog + " -Dthread=" + jthread)


if __name__ == "__main__":
    jmx = sys.argv[1]
    log = sys.argv[2] + "_" + sys.argv[5] + "u" + my_time()
    path = sys.argv[3]
    run_time = sys.argv[4]
    thread = sys.argv[5]
    schedule = sched.scheduler(time.time, time.sleep)
    schedule.enter(float(run_time), 0, run_jmeter, (jmx, log, path, thread))
    print '测试开始,当前时间:', time.time()
    print schedule.queue[0]
    schedule.run()
    os.remove(log)
