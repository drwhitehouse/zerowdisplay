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

def status(my_x, my_time, red, green, blue):
    """ new style status """
    for my_y in range(height):
        unicorn.set_pixel(my_x, my_y, red, green, blue)
        unicorn.show()
        time.sleep(my_time / height)
    for my_y in range(height):
        unicorn.set_pixel(my_x, my_y, 0, 0, 0)
    unicorn.show()

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
                s = threading.Thread(status(7, 30, red, green, blue))

class Attack(Resource):
    """ attacking """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(status(6,60,125,75,75))

class Challenge(Resource):
    """ challenge """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(status(5,90,75,255,75))

class Slay(Resource):
    """ slay """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(status(4,120,65,85,255))

class Fight(Resource):
    """ fighting """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(status(3,90,255,75,255))

class Notice(Resource):
    """ noticing """
    def get(self):
        hour = datetime.datetime.today().hour
        if hour < 6:
            s = threading.Thread(clear())
        else:
            s = threading.Thread(status(2,30,225,175,75))

class Slugs(Resource):
    """ Slugs """
    def get(self,red,green,blue):
        s = threading.Thread(status(0,150,red,green,blue))

class Test(Resource):
    """ testing """
    def get(self):
        s = threading.Thread(status(0,15,255,0,0))

api.add_resource(Activity, "/ac")
api.add_resource(Notice, "/no")
api.add_resource(Attack, "/at")
api.add_resource(Challenge, "/ch")
api.add_resource(Slay, "/sl")
api.add_resource(Fight, "/ft")
api.add_resource(Slugs, "/slug/<int:red>/<int:green>/<int:blue>")
api.add_resource(Test, "/test")

if __name__ == "__main__":
    app.run(host="10.15.0.11", debug=True)
