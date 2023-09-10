import socket
import os

host = "192.168.100.18"
port = 6667


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((host, port))
    s.listen()

    while True:

        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")
            
            message = ""
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                message = message + str(data)
                
            if message == "stop":
                os.system("shutdown")

        conn.close()

