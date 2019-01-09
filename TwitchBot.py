import socket
import time
import os
from threading import Thread

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'shinobot'
token = os.environ['TWITCH_TOKEN']
channel = '#volts__'

sock = socket.socket()
sock.connect((server, port))
sock.send("PASS {}\n".format(token).encode('utf-8'))
sock.send("NICK {}\n".format(nickname).encode('utf-8'))
sock.send("JOIN {}\n".format(channel).encode('utf-8'))

def timer(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 65432))
        s.sendall("{} {}".format(command, 1).encode("utf-8"))

    time.sleep(10)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 65432))
        s.sendall("{} {}".format(0, 0).encode("utf-8"))

while True:
    resp = sock.recv(2048).decode('utf-8')
    print(resp)
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))

    message = resp.split(":")[-1].rstrip()

    if message.startswith("!"):
        timerthread = Thread(target=timer, args=[message[1:]])
        timerthread.start()
