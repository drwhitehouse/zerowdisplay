#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Api, Resource
import random
import threading
import time
import unicornhat as unicorn
import numpy as np

# Define some variables

app = Flask(__name__)
api = Api(app)
sem = threading.Semaphore()

unicorn.rotation(0)
unicorn.brightness(0.5)
unicorn.set_layout(unicorn.AUTO)
width, height = unicorn.get_shape()

def clear():
    """ clear hat """
    unicorn.set_all(0, 0, 0)
    unicorn.show()

def status(my_x, my_time, load):
    """ new style status """
    red = load
    blue = 150
    green = 175
    sem.acquire()
    myArray = gethat()
    myArray = shifthat(myArray)
    sethat(myArray)
    my_load = display_percentage(load, height)
    for my_y in range(my_load):
        unicorn.set_pixel(my_x, my_y, red, green, blue)
        unicorn.show()
        time.sleep(my_time / height)
    unicorn.show()
    sem.release()

def flash(red, green, blue):
    """ new style flash """
    sem.acquire()
    myArray = gethat()
    clear()
    time.sleep(1)
    for _ in range(0, 15):
        unicorn.set_all(red, green, blue)
        unicorn.show()
        time.sleep(0.5)
        clear()
        time.sleep(0.5)
    time.sleep(1)
    sethat(myArray)
    sem.release()

def getrot(width, height):
    """ Get rotation """
    if width == height:
        myrot = random.randrange(0, 360, 90)
    else:
        myrot = random.randrange(0, 270, 180)
    return myrot

def gethat():
    """ Get Hat State """
    myArray = np.zeros((3,8,8), np.uint8)
    for x in range (width):
        for y in range (height):
            r, g, b = getpixel(x,y)
            myArray[0, x, y] = r
            myArray[1, x, y] = g
            myArray[2, x, y] = b
    return myArray

def sethat(myArray):
    """ Set Hat State """
    for x in range (width):
        for y in range (height):
            r = int(myArray[0,x,y])
            g = int(myArray[1,x,y])
            b = int(myArray[2,x,y])
            unicorn.set_pixel(x, y, r, g, b)
    unicorn.show()

def shifthat(myArray):
    """ shift hat one column right """
    for x in range (1,width):
        for y in range (height):
            myArray[0,x - 1,y] = myArray[0,x,y]
            myArray[1,x - 1,y] = myArray[1,x,y]
            myArray[2,x - 1,y] = myArray[2,x,y]
    for y in range (height):
        myArray[0,width -1,y] = 0
        myArray[1,width -1,y] = 0
        myArray[2,width -1,y] = 0
    return myArray

def getcoords(width, height):
    """ Gets random coords """
    xcoord = random.randint(0, width - 1)
    ycoord = random.randint(0, height - 1)
    return [xcoord, ycoord]

def getpixel(x, y):
    """ get pixel colour """
    r, g, b = unicorn.get_pixel(x, y)
    return r, g, b

def getcolour():
    """ gets a random colour """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return[red, green, blue]

def light_points(red, green, blue):
    """ pick random coords and light them """
    sem.acquire()
    myArray = gethat()
    clear()
    time.sleep(1)
    for _ in range(0, 30):
        my_x, my_y = getcoords(width, height)
        unicorn.set_pixel(my_x, my_y, red, green, blue)
        unicorn.show()
        time.sleep(0.25)
    clear()
    time.sleep(1)
    sethat(myArray)
    sem.release()

class Activity(Resource):
    """ activity """
    def get(self, load):
        status(width - 1, 30, load)

class Points(Resource):
    """ Points """
    def get(self, red, green, blue):
        light_points(red, green, blue)

class Flash(Resource):
    """ Flash """
    def get(self):
        red, green, blue = getcolour()
        flash(red, green, blue)

class Bedtime(Resource):
    """ clear hat """
    def get(self):
        clear()

def display_percentage(percentage, display):
    """work out how many leds to light"""
    return int(float(percentage) * float(display) / 100)

api.add_resource(Activity, "/ac/<int:load>")
api.add_resource(Points, "/pt/<int:red>/<int:green>/<int:blue>")
api.add_resource(Flash, "/flash")
api.add_resource(Bedtime, "/bedtime")

if __name__ == "__main__":
    app.run(host="10.15.0.11", debug=True)
