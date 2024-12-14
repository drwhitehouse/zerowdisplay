#!/usr/bin/env python3

""" raspberry pi zero w unicorn hat cpu monitor """

import psutil
import requests

def send_loadavg(url, load):
    """ send the loadavg """
    my_url = url + str(load)
    requests.get(my_url, timeout=60)

def get_loadavg():
    """get the 5 minute loadavg as percentage"""
    my_loadavg = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
    return my_loadavg[1]

def sample_cpu():
    """get cpu utilisation"""
    return psutil.cpu_percent(interval=1)

def main(url):
    """start here"""
    my_cpu = sample_cpu()
    my_avg = int(get_loadavg())
    send_loadavg(url, my_avg)
    print(f"CPU UTILISATION : {my_cpu} %")
    print(f"LOADAVG 5min    : {my_avg} %")

if __name__ == "__main__":
    URL = 'http://chowfaan.hot.dim-sum.home:5000/ac/'
    main(URL)
