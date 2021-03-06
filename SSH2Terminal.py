# SSH's into address' terminal

import socket
from ssh2.session import Session

host = input('ip: ')
user = input('user: ')
password = input('pw: ')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 22))

session = Session()
session.handshake(sock)
session.userauth_password(user, password)

channel = session.open_session()
channel.execute(input('cmd: '))
size, data = channel.read()
while size > 0:
    print(data.decode())
    size, data = channel.read()
channel.close()
print('Data Transmission: Complete.')
