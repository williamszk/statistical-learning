import socket


while True:

    HOST = "127.0.0.1"
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_conn:
        socket_conn.bind((HOST, PORT))
        socket_conn.listen()

        print("The program will wait for some request.")
        conn, addr = socket_conn.accept() # the run time will wait here for some connection request

        with conn:
            print(f"Connect by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
