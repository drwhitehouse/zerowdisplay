#!/usr/bin/env python3

""" raspberry pi zero w unicorn hat lightshow trigger """

import uhs_utils
import argparse
import requests

def request_pt(red, green, blue):
    """ request pt """
    my_url = url + "pt/" + str(red) + "/" + str(green) + "/" + str(blue)
    print(my_url)
    requests.get(my_url)

url = 'http://chowfaan.hot.dim-sum.home:5000/'
my_red, my_green, my_blue = uhs_utils.getcolour()

parser = argparse.ArgumentParser(description='Lightshow Lizard')
parser.add_argument('--pt', action='store_true', dest='pt', help='trigger uhs Points')
parser.add_argument('--bed', action='store_true', dest='bed', help='trigger uhs Bed')
parser.add_argument('--red', type=int, default=my_red)
parser.add_argument('--green', type=int, default=my_green)
parser.add_argument('--blue', type=int, default=my_blue)
args = parser.parse_args()

if args.pt:
    my_red = args.red
    my_green = args.green
    my_blue = args.blue
    request_pt(my_red, my_green, my_blue)
else:
    print("Nothing to do...")
