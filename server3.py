import socket
import threading
import sys
import cv2

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
                imageData = None

                #f = open("recieved.jpg", "wb")

                #f.write(data)

                #f.close()

                print("Done receiving")
                frame = cv2.imread("recieved.jpg")  # read the video in frames
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert each frame to grayscale.
                blur = cv2.GaussianBlur(gray, (5, 5), 0)  # blur the grayscale image
                ret, th1 = cv2.threshold(blur, 35, 255,
                                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # using threshold remove noise
                ret1, th2 = cv2.threshold(th1, 127, 255, cv2.THRESH_BINARY_INV)  # invert the pixels of the image frame
                contours, hierarchy = cv2.findContours(th2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find the contours
                result = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
                # cv2.imshow('frame',frame) #show video

                cv2.imshow("result", result)  # display image
                cv2.waitKey(0)

                # address = str(input('ip: '))

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
                    connection.send(bytes(input("l"), 'utf-8'))
                    print("oi")

                elif cx >= 170:
                    print("go right")
                    connection.send(bytes(input("r"), 'utf-8'))
                    print("oii")

                elif cx > 151 and cx < 169:
                    print("go straight")
                    connection.send(bytes(input("f"), 'utf-8'))
                    print("oiii")


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



