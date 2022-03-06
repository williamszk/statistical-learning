# Objective

Use the tutorial: https://realpython.com/python-sockets/

Build a server in an EC2 instance.
Write a client script to access the server in EC2 instance.


I don't know what this error means:
```python
My public IP address is: 15.228.58.28
Traceback (most recent call last):
  File "echo-server.py", line 13, in <module>
    socket_conn.bind((HOST, PORT))
OSError: [Errno 99] Cannot assign requested address
```

But I've read that we can't use a virtual machine for socket communication. Is this correct?