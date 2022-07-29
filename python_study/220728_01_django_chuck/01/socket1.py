# https://youtu.be/o0XbHvKxw7Y?t=2282
# an experiment with sockets
def main():
    import socket
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mysocket.connect(("data.pr4e.org", 80))
    # mysocket.connect((".pr4e.org", 80)) # socket.gaierror: [Errno -2] Name or service not known

    cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")

    mysocket.close()


if __name__ == "__main__":
    main()
