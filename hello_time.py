#!/usr/bin/python
# -*- coding: utf-8 -*-
#David Schroeder
#hello_time.py

#A program for infinitely proclaiming a greeting to the world
#and the current time.  Why anyone would want this is beyone me.

### Imports ###
import time  #For sleeping
import datetime #For getting current time

### Main Program ###

while True:
    thetime=datetime.datetime.now()

    print("Hello, world!  It is %s" % thetime)

    time.sleep(1) #Waits one second before repeating