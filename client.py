import socket
import threading
import sys


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPv4
    # address = '192.168.56.1'
    def __init__(self):
        self.sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg)  # assigns message [i]nput to a thread
        iThread.daemon = True  # .daemon kills thread when .py is closed
        iThread.start()  # starts thread
        while True:
            data = self.sock.recv(1024)  # message max length in bytes
            if not data:
                break
            print(str(data, 'utf-8'))

    def sendMsg(self):  # continually asks for input and then sends to the client
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

address = str(input('ip: '))
client = Client()
client.sendMsg()
