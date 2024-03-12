#!/usr/bin/env python3

""" functions for the unicorn hat servers """

import random

def getcolour():
    """ gets a random colour """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return[red, green, blue]

if __name__ == "__main__":
    print("uhs_utils.py")
