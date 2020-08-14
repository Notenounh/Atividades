#Client
from socket import *
import pybase64

host = ('', 56322)

while True:
    connction = socket(AF_INET, SOCK_STREAM)
    connction.connect((host))
    while True:
        msg = bytes(input("Type the message: "), 'utf-8')
        bytes_base64 = bytes(pybase64.b64encode(msg))
        connction.send(bytes_base64)
        resp = connction.recv(1024)
        resp = pybase64.b64decode(resp)
        print("Recived: ", resp)
    connction.close()
