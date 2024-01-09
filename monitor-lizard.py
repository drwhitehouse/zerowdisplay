#!/usr/bin/env python3

""" raspberry pi zero w unicorn hat cpu monitor """

import psutil
import requests
url = 'http://chowfaan.hot.dim-sum.home:5000/ac/'

def send_loadavg(load):
    """ send the loadavg """
    my_url = url + str(load)
    requests.get(my_url)

def get_loadavg():
    """get the 5 minute loadavg as percentage"""
    my_loadavg = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    return my_loadavg[1]

def sample_cpu():
    """get cpu utilisation"""
    return psutil.cpu_percent(interval=1)

my_cpu = sample_cpu()
my_avg = int(get_loadavg())
send_loadavg(my_avg)

print(f"LOADAVG 5min : {my_avg} %")
