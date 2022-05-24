import threading
import socket

SIZE = 1024
HOST = '127.0.0.1'
PORT = 12345
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn , addr):
    connected = True
    print("[CONNECT] get connection {}".format(addr))
    while connected:
        get_msg = conn.recv(SIZE).decode()
        if get_msg != '':
            print(get_msg)
            if get_msg == "disconnect" :
                connected = False
            else:
                if get_msg[1] == "+":
                    toplam = (int(get_msg[0]) + int(get_msg[2]))
                    send_lenght = len(str(toplam))
                    bytes = str(toplam).encode() + (b'' * (SIZE - send_lenght))
                    conn.send(bytes)
                elif get_msg[1] == "-":
                    fark= (int(get_msg[0]) - int(get_msg[2]))
                    send_lenght = len(str(fark))
                    bytes = str(fark).encode() + (b'' * (SIZE - send_lenght))
                    conn.send(bytes)
                elif get_msg[1] == "*":
                    carpim = (int(get_msg[0]) * int(get_msg[2]))
                    send_lenght=len(str(carpim))
                    bytes= str(carpim).encode() + (b'' * (SIZE - send_lenght))
                    conn.send(bytes)
                elif get_msg[1] == "/":
                    bolüm = (int(get_msg[0]) // int(get_msg[2]))
                    send_lenght=len(str(bolüm))
                    bytes= str(bolüm).encode() + (b'' * (SIZE - send_lenght))
                    conn.send(bytes)                
    
    conn.close()




def main():
    print(f"[Listening] server on {ADDR} listening...")
    while True:
        server.listen()
        conn, addr = server.accept()

        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()


main()
