# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:45:20 2019

@author: Alec
"""

import cv2
import socket
import time

imageFileName = "recieved.jpg"


def recieveImage(imageFileName):

    while True:
        try:
            socketImage = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socketImage.connect(('192.168.0.119', 12343))
            print("Established connection.")
            print("Recieving picture")
            break
        except ConnectionRefusedError as e:
            x = 1

    # here you must past the public external ip address of the server machine, not that local address
    f = open(imageFileName, "wb")
    data = None
    while True:
        m = socketImage.recv(1024)
        #print(m)
        data = m
        if m:
            while m:
                m = socketImage.recv(1024)
                data += m
            else:
                break
    f.write(data)

    f.close()

    print("Done recieving")


    
    
def getContours(imageFileName):
    print("processing image")
    frame = cv2.imread(imageFileName) # read the video in frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert each frame to grayscale.
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # blur the grayscale image
    blur = cv2.GaussianBlur(blur, (5, 5), 0)  # blur the grayscale image
    blur = cv2.GaussianBlur(blur, (5, 5), 0)  # blur the grayscale image
    ret, th1 = cv2.threshold(blur, 35, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # using threshold remove noise
    ret1, th2 = cv2.threshold(th1, 127, 255, cv2.THRESH_BINARY_INV)  # invert the pixels of the image frame
    contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find the contours
    result = cv2.drawContours(blur, contours, -1, (0, 255, 0), 3)
    # cv2.imshow('frame',frame) #show video

    cv2.imshow("result", result)  # display image
    cv2.waitKey(0)
    return contours

def getAction(contours):
    print("Lets See our options")
    for cnt in contours:
        if cnt is not None:
            area = cv2.contourArea(cnt)  # find the area of contour
        if area >= 500:
            # find moment and centroid
            M = cv2.moments(cnt)
            cx = int(M['m10'] / M['m00'])
            #cy = int(M['m01'] / M['m00'])

    print(cx)
    #changeInPixel = 0.49
    if cx < 590:
        
        return "l"

    elif cx >= 590 and cx <= 680:
        return "f"

    elif cx > 680:
        return "r"
    
    else:
        return None

def sendAction(action, socket):
    print("Sending Action.")
    if action is not None:
        connection.send(bytes(action, 'utf-8'))
#while True:



connection = []
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('0.0.0.0', 12344))
print("socket binding")
serverSocket.listen(10)
connection, addr = serverSocket.accept()
print("accecpted connection")



while True:
    recieveImage(imageFileName)

    # m = c.recv(1024)
    # print(m)
    # print(getAction(contours))

    contours = getContours(imageFileName)
    action = getAction(contours)
    print(action)
    sendAction(action, serverSocket)



serverSocket.close()
connection.close()
