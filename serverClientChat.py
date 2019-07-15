# LE: 05/19/2019; chat.py

import socket
import threading
import sys

# to connect as a client run chat.py (server address) in cmd
# for more info on socket, visit https://www.openssh.com/txt/socks4.protocol

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # .socket(CONNECTION_TYPE(IPV6, etc.), PARAM2)
    connections = []  # list of connected clients

    def __init__(self):
        self.sock.bind(('0.0.0.0', 10000))
        self.sock.listen(3)  # listens for connections made to the socket (1-5)

    def handler(self, c, a):  # sends data to client
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break


    def run(self):
        while True:
            c, a = self.sock.accept()
            sThread = threading.Thread(target=self.handler, args=(c, a))  # assigns the [s]erver to a thread
            sThread.daemon = True
            sThread.start()
            self.connections.append(c)
            print(str(a[0])+ ':' + str(a[1]), "connected")


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPv4

    def __init__(self, address):
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


if len(sys.argv) > 1:  # creates instance of client
    client = Client(sys.argv[1])
else:  # creates instance of server
    ultron = Server()
    ultron.run()
