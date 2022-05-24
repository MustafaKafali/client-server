import os
import socket


SIZE = 1024
HOST = '127.0.0.1'
PORT = 12345
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect_ex(ADDR)


def send():
    send_data= input("Veri giriniz (x+y) veya (x/y) şeklinde...\n")
    send_lenght = len(send_data)
    bytes = send_data.encode() + (b'' * (SIZE - send_lenght))
    client.send(bytes)
    get_data = client.recv(SIZE).decode()
    print(get_data)
    dosya = open("Dosya.txt","w")
    dosya.write(get_data)
    dosya.close
        




send()
