# merges cv2Countours.py with client.py to send instructions to the robo
# to be used on Ultron


import socket
import threading
import sys
import time
import cv2



class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPv4
    # address = '192.168.56.1'

    def __init__(self):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg)  # assigns message [i]nput to a thread
        iThread.daemon = True  # .daemon kills thread when .py is closed
        iThread.start()  # starts thread

        robo_functions.init()
        
        while True:
            data = self.sock.recv(1024)  # message max length in bytes
            if not data:
                print("Connection terminated.")
                break

            frame = cv2.imread("recieved.jpg")  # read the video in frames # todo collect .jpg from robo
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert each frame to grayscale.
            blur = cv2.GaussianBlur(gray, (5, 5), 0)  # blur the grayscale image
            ret, th1 = cv2.threshold(blur, 35, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # using threshold remove noise
            ret1, th2 = cv2.threshold(th1, 127, 255, cv2.THRESH_BINARY_INV)  # invert the pixels of the image frame
            contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find the contours
            # result = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)


            for cnt in contours:
                if cnt is not None:
                    area = cv2.contourArea(cnt)  # find the area of contour
                if area >= 500:
                    # find moment and centroid
                    M = cv2.moments(cnt)
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])

            if cx <= 150:
                print("go left")
                self.sock.send(bytes(input("l"), 'utf-8')) # todo: fix robo chat string

            elif cx >= 170:
                print("go right")
                self.sock.send(bytes(input("r"), 'utf-8')) # todo: fix robo chat string

            elif cx > 151 and cx < 169:
                print("go straight")
                self.sock.send(bytes(input("f"), 'utf-8')) # todo: fix robo chat string

            print(str(data, 'utf-8'))
            
    def sendMsg(self):  # continually asks for input and then sends to the client
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))
            


address = str(input('ip: '))
client = Client()
client.sendMsg()


