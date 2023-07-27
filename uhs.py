#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Api, Resource
import datetime
import random
import threading
import time
import unicornhat as unicorn
import ipaddress

# Define some variables

app = Flask(__name__)
api = Api(app)

unicorn.rotation(0)
unicorn.brightness(0.5)
unicorn.set_layout(unicorn.AUTO)
width, height = unicorn.get_shape()

def clear():
    """ clear hat """
    unicorn.set_all(0, 0, 0)
    unicorn.show()

def activity(width, height, red, green, blue):
    """ Activity """
    myrot = getrot(width, height)
    myrandom = random.randint(0, 1)
    mytime = 30
    unicorn.rotation(myrot)
    for my_x in range(width):
        for my_y in range(height):
            unicorn.set_pixel(my_x, my_y, red, green, blue)
        unicorn.show()
        if myrandom > 0:
            for myother_x in range(width):
                for myother_y in range(height):
                    unicorn.set_pixel(myother_x, myother_y, 0, 0, 0)
        time.sleep(mytime / width)
    unicorn.set_all(0, 0, 0)
    unicorn.show()

def mycolour(red, green, blue):
    """ make mycolour """
    for _ in range(5):
        unicorn.set_all(red, green, blue)
        unicorn.show()
        time.sleep(1)
        clear()
        time.sleep(1)

def get_address_fam(address):
    addr = ipaddress.ip_address(address)
    version = addr.version
    return version

def split_address(address):
    REQ=[]
    for value in address.split("."):
        REQ.append(int(value))
    return REQ

def colourfromip(red, green, blue, four):
    red = red ^ four + 100
    blue = blue ^ four + 100
    green = green ^ four + 100
    return red, green, blue

def getrot(width, height):
    """ Get rotation """
    if width == height:
        myrot = random.randrange(0, 360, 90)
    else:
        myrot = random.randrange(0, 270, 180)
    return myrot

class Activity(Resource):
    """ activity """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            address = request.remote_addr
            fam = get_address_fam(address)
            if fam == 4:
                REQ = split_address(address)
                red, green, blue = colourfromip(REQ[0], REQ[1], REQ[2], REQ[3])
                s = threading.Thread(activity(width, height, red, green, blue))

class Attack(Resource):
    """ attacking """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(mycolour(125,75,75))

class Challenge(Resource):
    """ challenge """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(mycolour(75,125,75))

class Fight(Resource):
    """ fighting """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(mycolour(255,0,0))

api.add_resource(Activity, "/ac")
api.add_resource(Attack, "/at")
api.add_resource(Challenge, "/ch")
api.add_resource(Fight, "/ft")

if __name__ == "__main__":
    app.run(host="10.15.0.11", debug=True)
