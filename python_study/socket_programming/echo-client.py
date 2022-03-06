# echo-client.py

import socket
import time
from tqdm import tqdm


elapsed_times = []

HOST = "127.0.0.1" # Server IP address
PORT =  65432 # the port open for connection in the server

for _ in tqdm(range(100)):
    time.sleep(0.1)
    start = time.perf_counter()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_conn:
        socket_conn.connect((HOST, PORT))
        socket_conn.sendall(b"k"*1000)
        data = socket_conn.recv(1024)

    print(f"Received {data!r}")

    elapsed_times.append(time.perf_counter() - start)

import pandas as pd
print(pd.Series(elapsed_times).describe())


# count    100.000000
# mean       0.000887
# std        0.000362
# min        0.000299
# 25%        0.000694
# 50%        0.000825
# 75%        0.001046
# max        0.002527

# we can try to create the server script in an EC2 instance 
# then we can try to access it using the client

# ssh -i "/home/william/Documents/samsungec2tutorial.pem" ubuntu@15.228.58.28