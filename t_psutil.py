#!/usr/bin/python
# -*- coding:utf-8 -*-

import psutil
import time

cpu = psutil.cpu_percent(interval=1)
memory = float(psutil.virtual_memory().used) / float(psutil.virtual_memory().total) * 100.0
last_disk = psutil.disk_io_counters(perdisk=False).read_bytes + psutil.disk_io_counters(perdisk=False).write_bytes
last_network = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().packets_recv
time.sleep(1)
disk = (psutil.disk_io_counters(perdisk=False).read_bytes + psutil.disk_io_counters(
    perdisk=False).write_bytes - last_disk) / 1024
network = (psutil.net_io_counters().bytes_sent + psutil.net_io_counters().packets_recv - last_network) / 1024
print('cpu:', cpu, 'memory:', memory, 'disk:', disk, 'network:', network)
