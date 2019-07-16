# todo: verify if it takes a photo and sends it to other clients


import socket
import threading
import robo_functions
import picamera
import os

def imageCapture():
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.capture("/home/pi/stuRobo2/image1.jpg")

def imageSend():
    f = open("image1.jpg", "rb")
    l = os.path.getsize("image1.jpg")
    m = f.read(l)
    Client.sock.send(m)
    f.close()

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

            tf = 1
            ts = 1.1
            tx = 0.2

            if (str(data, 'utf-8')) == 'f':
                robo_functions.forward(tf)
                robo_functions.sit(tf)
                imageCapture()
                imageSend()

            if (str(data, 'utf-8')) == 's':
                robo_functions.sit(tf)
                imageCapture()
                imageSend()

            if (str(data, 'utf-8')) == 'rv':
                robo_functions.reverse(tf)
                robo_functions.sit(tf)
                imageCapture()
                imageSend()

            if (str(data, 'utf-8')) == 'l':
                robo_functions.pivot_left(ts)
                robo_functions.sit(tf)
                imageCapture()
                imageSend()

            if (str(data, 'utf-8')) == 'r':
                robo_functions.pivot_right(tx)
                robo_functions.sit(tf)
                imageCapture()
                imageSend()

            print(str(data, 'utf-8'))
            
    def sendMsg(self):  # continually asks for input and then sends to the client
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))
            


address = str(input('ip: '))
client = Client()
client.sendMsg()


