#!/usr/bin/env python3

""" raspberry pi zero w unicorn hat lightshow trigger """

import argparse
import requests
import uhs_utils

def request_pt(red, green, blue):
    """ request pt """
    my_url = URL + "pt/" + str(red) + "/" + str(green) + "/" + str(blue)
    print(my_url)
    requests.get(my_url, timeout=120)

def request_flash(red, green, blue):
    """ request flash """
    my_url = URL + "flash/" + str(red) + "/" + str(green) + "/" + str(blue)
    print(my_url)
    requests.get(my_url, timeout=120)

def request_bed():
    """ request bed """
    my_url = URL + "bedtime"
    print(my_url)
    requests.get(my_url, timeout=120)

def main():
    """ start here """
    if args.pt:
        this_red = args.red
        this_green = args.green
        this_blue = args.blue
        request_pt(this_red, this_green, this_blue)
    elif args.flash:
        this_red = args.red
        this_green = args.green
        this_blue = args.blue
        request_flash(this_red, this_green, this_blue)
    elif args.bed:
        request_bed()
    else:
        print("Nothing to do...")

if __name__ == "__main__":
    URL = 'http://chowfaan.hot.dim-sum.home:5000/'
    my_red, my_green, my_blue = uhs_utils.getcolour()
    parser = argparse.ArgumentParser(description='Lightshow Lizard')
    parser.add_argument('--pt', action='store_true', dest='pt', help='trigger uhs Points')
    parser.add_argument('--flash', action='store_true', dest='flash', help='trigger uhs Flash')
    parser.add_argument('--bed', action='store_true', dest='bed', help='trigger uhs Bed')
    parser.add_argument('--red', type=int, default=my_red)
    parser.add_argument('--green', type=int, default=my_green)
    parser.add_argument('--blue', type=int, default=my_blue)
    args = parser.parse_args()
    main()
