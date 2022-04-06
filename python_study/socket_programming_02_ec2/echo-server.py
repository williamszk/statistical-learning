import socket
import requests

PUBLIC_IP = requests.get("https://api.ipify.org").content.decode("utf8")
print(f"My public IP address is: {PUBLIC_IP}")

while True:
    
    HOST = PUBLIC_IP
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_conn:
        socket_conn.bind((HOST, PORT))
        socket_conn.listen()

        print("The program will wait for some request.")

        conn, addr = socket_conn.accept()

        with conn:
            print(f"Connect by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)