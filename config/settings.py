# -*- coding: utf-8 -*-

# 定义操作指令
STOP     = 0x0000
LEFT     = 0x0001
RIGHT    = 0x0010
FORWARD  = 0x0100
BACKWARD = 0x1000
SHUTDOWN = 0x1111

SERVER_HOST = "0.0.0.0"
PI_HOST = "172.17.11.169"
COMPUTER_HOST = "172.17.11.102"
VIDEO_STREAMING_PORT = 8000
KEYBOARD_PORT = 8001


# 设定摄像头拍摄的图像大小
RESOLUTION = (640, 480)

IMAGE_DIR = "../training_images"
SAMPLE_DIR = "../training_data"
