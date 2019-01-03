# -*- coding: utf-8 -*-

import os
import socket
import struct
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../")
from config.settings import *


class KeyboardServer(object):
    def __init__(self, host, port):
        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)
        self.connection = self.server_socket.accept()[0]
        print("Keyboard Socket Connected!")

    def receive(self):
        code2str = {
            0x0000: "Stop",
            0x0001: "Left",
            0x0010: "Right",
            0x0100: "Forward",
            0x0101: "Forward Left",
            0x0110: "Forward Right",
            0x1000: "Backward",
            0x1001: "Backward Left",
            0x1010: "Backward Right",
            0x1111: "Shutdown"
        }
        while True:
            op = struct.unpack('<I', self.connection.recv(struct.calcsize('<I')))[0]
            print("Receive: %s" % code2str[op])
            if op == SHUTDOWN:
                self.connection.close()
                print("Connection Closed!")
                sys.exit(0)


if __name__ == "__main__":
    server = KeyboardServer(host=SERVER_HOST, port=KEYBOARD_PORT)
    server.receive()
