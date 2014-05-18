#!/usr/bin/env python


import time, sys,serial


s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/ttyAMA0"

try:
    s.open()
except serial.SerialException, e:
    sys.stderr.write("could not open port %r: %s\n" % (s.port, e))
    sys.exit(1)

s.write("$$$ALL,OFF\r")

#######################
x=0
y=126

#Dessin pour des test: im2="$$$F000000011111100000000111000011111110011111110111111111111111111111111111011111110011111110000111000000000000000000000000000000\r"
#######################

time.sleep(0.5)
while (x<126):
    x=x+1
    time.sleep(0.01)
    im0=x*"1"+(126-x)*"0"
    im1="$$$F"+im0+"\r"
    s.write(im1)

time.sleep(0.5)

while (y>0):
    y=y-1
    time.sleep(0.01)
    im00=(126-y)*"0"+(y*"1")
    im2="$$$F"+im00+"\r"
    s.write(im2)

