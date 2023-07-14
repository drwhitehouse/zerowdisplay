#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api, Resource
import datetime
import random
import threading
import time
import unicornhat as unicorn

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

def red():
    """ make red """
    unicorn.set_all(255, 0, 0)
    unicorn.show()

class Illuminate(Resource):
    """ illuminate """
    def get(self):
        red()

class UnIlluminate(Resource):
    """ Unilluminate """
    def get(self):
        clear()

api.add_resource(Illuminate, "/il")
api.add_resource(UnIlluminate, "/ul")

if __name__ == "__main__":
    app.run(host="10.15.0.11", debug=True)
