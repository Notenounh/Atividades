#Servidor
import pybase64
from socket import *

servidor = ('', 56322)

#AF_INET para conexão ip / dns - SOCK_STREAM conexão tcp
connection = socket(AF_INET, SOCK_STREAM)
#Bind espera a conexão do que vem a frente
connection.bind((servidor))
#Listen define quantas pessoas terão na interação
connection.listen(2)

print("Waiting connection...")
while True: 
    con, client = connection.accept()
    print("Connected", client)
    while True:
        msg_recived = con.recv(1024)
        decode_base64 = pybase64.b64decode(msg_recived)
        print("Client said: ", decode_base64)
        
        msg_send = bytes(input("Type the message: "), 'utf-8')
        bytes_base64 = bytes(pybase64.b64encode(msg_send))
        con.send(bytes_base64)
    con.close()
