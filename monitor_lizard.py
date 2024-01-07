#!/usr/bin/env python3

""" raspberry pi zero w unicorn hat cpu monitor """

import psutil

#print(f"CPU utilization: {psutil.cpu_percent()}%")
#print(f"Memory utilization: {psutil.virtual_memory().percent}%")
#print(f"CPU: {psutil.cpu_times()}")
#print(f"CPU: {psutil.cpu_percent(interval=1, percpu=True)}")
#print(f"CPU: {psutil.cpu_percent(interval=1)}")

VERTICAL=4
HORIZONTAL=8

def display_percentage(percentage, display):
    """work out how many leds to light"""
    return int(float(percentage) * float(display) / 100)

def sample_cpu():
    """get cpu utilisation"""
    return psutil.cpu_percent(interval=1)

my_cpu = sample_cpu()

print(f"CPU Percentage: {my_cpu}")
print(f"Which would be {display_percentage(my_cpu, VERTICAL)} leds lit vertically, \
or {display_percentage(my_cpu, HORIZONTAL)} horizontally.")
