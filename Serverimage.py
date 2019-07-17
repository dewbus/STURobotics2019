# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:23:35 2019

@author: Alec
"""
import time
import socket
import os

""""
with picamera.PiCamera() as camera:
     camera.resolution = (1280, 720)
     camera.capture("/home/pi/stuRobo2/image1.jpg")

"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((input('ip: '), 10000)) # if the clients/server are on different network you shall bind to ('', port)



print('connected')



f = open("image1.jpg", "rb")

l = os.path.getsize("image1.jpg")
print(l)
m = f.read(l)

s.send(bytes(m))

f.close()

print("Done sending...")


