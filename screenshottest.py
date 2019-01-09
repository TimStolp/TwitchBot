import time
import cv2
import mss
import numpy as np
import select
import socket
import random

on = False


def flip(img, start_h, end_h, start_w, end_w):
    img[start_h:end_h, start_w:end_w, :] = np.rot90(
        img[start_h:end_h, start_w:end_w, :],
        random.randint(0,3),
        (0,1)
    )


def r_color(img, start_h, end_h, start_w, end_w):
    np.take(
        img[start_h:end_h, start_w:end_w, :],
        np.random.permutation(img[start_h:end_h, start_w:end_w, :].shape[2]),
        axis=2,
        out=img[start_h:end_h, start_w:end_w, :]
    )


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 65432))
    sock.listen()
    with mss.mss() as sct:
        read_list = [sock]
        write_list = []
        exception_list = []
        while True:
            readable, writable, errored = select.select(read_list, write_list, exception_list, 0)
            for s in readable:
                if s is sock:
                    conn, addr = s.accept()
                    with conn:
                        # print('Connected by', addr)
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            command, filter_switch = data.decode("utf-8").split(" ")
                            if int(filter_switch) == 1:
                                on = True
                            elif int(filter_switch) == 0:
                                on = False

            last_time = time.time()

            size = sct.monitors[0]
            #size = {'left': 0, 'top': 0, 'width': 800, 'height': 480}
            img = np.array(sct.grab(size))

            if on:
                if command == 'deathsimulator':
                    for w in range(0, 800, 160):
                        for h in range(0, 480, 160):
                            flip(img, h, h+160, w, w+160)
                if command == 'clown':
                    img += random.randint(0, 100)
                if command == 'rainbow':
                    for w in range(0, 800, 160):
                        for h in range(0, 480, 160):
                            r_color(img, h, h+160, w, w+160)
                if command == 'test':
                    for w in range(0, 1920-160, 160):
                        for h in range(0, 1080-160, 160):
                            flip(img, h, h+160, w, w+160)
                            r_color(img, h, h+160, w, w+160)

            cv2.imshow("OpenCV/Numpy normal", img)

            print("fps: {}".format(1 / (time.time() - last_time)))

            # Press "=" to quit
            if cv2.waitKey(25) & 0xFF == 61:
                cv2.destroyAllWindows()
                break
