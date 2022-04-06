import time
import socket

import requests

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 22223        # Port to listen on (non-privileged ports are > 1023)

# set start time and length of time
start = time.time()
PERIOD_OF_TIME = 3600 # 60 min

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            if time.time() < start + PERIOD_OF_TIME: # run as long as time.time() is less than the start plus 60 minutes
                data = requests.get('http://api.open-notify.org/iss-now.json').text
                conn.sendall(str.encode(data+'\n'))
                time.sleep(10)
            else:
                 break
