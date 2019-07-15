# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:03:36 2019

@author: Alec
"""

#Client side
import socket                   # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("172.20.220.224", 12345)) # here you must past the public external ipaddress of the server machine, not that local address
print("finding port")

f = open("recieved.jpg", "wb")
print("opening jpg")
data = None

while True:

    m = s.recv(1024)

    data = m

    if m:

        while m:

            m = s.recv(1024)

            data += m

        else:

            break

f.write(data)

f.close()

print("Done receiving")