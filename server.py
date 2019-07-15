import socket
import threading
import sys

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
            sThread = threading.Thread(target=self.handler, args=(c, a))  # assigns the server to a thread
            sThread.daemon = True
            sThread.start()
            self.connections.append(c)

            robots = 0

            for address in a:
                s = []
                roboCount = robots
                s.append("Robo " + str(roboCount))
                robots = robots + 1


            print(s[0])

            print(str(a[0]) + ':' + str(a[1]), "connected")



host = Server()
host.run()



