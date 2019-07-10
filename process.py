#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 参考链接：https://blog.csdn.net/liitdar/article/details/81076128
# Description: 用于获取操作系统的进程信息
# Created on: 2019-04-09
# Author: yyr

import psutil
import os
import time

#print("------------------------show all processes info----------------------")
# get all pid
pids = psutil.pids()
with open('/home/yyr/process/process_info.txt','a') as f:
    for pid in pids:
        # get process by pid
        p = psutil.Process(pid)
        # get process name by process
        process_name = p.name()
        # 内存利用率
        memory_usage = p.memory_percent()
        # CPU使用率
        cpu_usage = p.cpu_percent()
        # 磁盘使用情况
        disk_usage = psutil.disk_usage('/')
        # 磁盘IO
        disk_io = psutil.disk_io_counters()
    
        #print ("Crrrent time: "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #print("Process name: %s, pid: %s, memory_usage: %.2f%%, cpu_usage: %.2f%%, disk_usage: %s, disk_io: %s" %(process_name,pid,memory_usage,cpu_usage,disk_usage,disk_io))
        
        print("------------------------show all processes info----------------------", file=f)
        print("Current time: "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), file=f)
        print("Process name: %s\n pid: %s\n memory_usage: %.2f%%\n cpu_usage: %.2f%%\n disk_usage: %s\n disk_io: %s\n" %(process_name,pid,memory_usage,cpu_usage,disk_usage,disk_io), file=f)
    
exit(0)
