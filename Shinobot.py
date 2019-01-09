import socket
import os

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'shinobot'
token = os.environ['TWITCH_TOKEN']
channel = '#veigodeu'

sock = socket.socket()
sock.connect((server, port))
sock.send("PASS {}\n".format(token).encode('utf-8'))
sock.send("NICK {}\n".format(nickname).encode('utf-8'))
sock.send("JOIN {}\n".format(channel).encode('utf-8'))


while True:
    resp = sock.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))

    message = resp.split(":")[-1].rstrip()
    print(message)
    if message.startswith("!"):
        if message[1:] == 'test':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, message).encode('utf-8'))
        if message[1:] == 'VorReel':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, "haha @VorReel").encode('utf-8'))
        if message[1:] == 'laatch':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, "MOOOOOOOOOOOOOOOOOOOOOOOOOVVVVVEMEEEEEEEEENTS").encode('utf-8'))
        if message[1:] == 'metroid':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, "🥑 🥖").encode('utf-8'))
        if message[1:] == 'veteran':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, "washed up").encode('utf-8'))
        if message[1:] == 'funnel':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, "PLAY NASUS FUNNEL SwiftRage").encode('utf-8'))
        if message[1:] == 'wiowid':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, "dont care").encode('utf-8'))
        if message[1:] == 'wendy':
            sock.send("PRIVMSG {} :{}\r\n".format(channel, "boosted dutch egirl").encode('utf-8'))
