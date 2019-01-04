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

modes = {"test": 1, "clown": 2}
global on
on = False
global command
command = 0


def timer():
    global on
    on = True
    time.sleep(5)
    on = False


def overlay():
    global command
    global on
    while True:
        if on:
            if command == 1:
                while on:
                    print("test")
                    time.sleep(1)
            elif command == 2:
                while on:
                    print("test2")
                    time.sleep(1)


def default():
    global on
    while True:
        if not on:
            print("default")
            time.sleep(1)


p1 = Thread(target=default)
p1.start()
p2 = Thread(target=overlay)
p2.start()
while True:
    resp = sock.recv(2048).decode('utf-8').split(":")[-1].rstrip()
    print(resp)
    if resp.startswith("!"):
        command = modes[resp[1:]]
        resp = ""
        p3 = Thread(target=timer)
        p3.start()
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))