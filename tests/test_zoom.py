"""
@file test_center_gimbal.py
@Description: This is a test script for using the SIYI SDK Python implementation to adjust zoom level
@Author: Mohamed Abdelkader
@Contact: mohamedashraf123@gmail.com
All rights reserved 2022
"""

import sys
import os
from time import sleep

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)

sys.path.append(parent_directory)

from siyi_sdk import SIYISDK


def test():
    cam = SIYISDK(server_ip="192.168.144.25", port=37260)

    if not cam.connect(maxWaitTime=10):
        print("No connection ")
        exit(1)

    cam.requestZoomLevel(4.5)
    sleep(3)
    # print("Zoom level: ", cam.getZoomLevel())
    #
    # # cam.requestCenterGimbal()
    # # cam.requestLockMode()
    # cam.sendMsg("55 66 01 02 00 01 00 0F 04 05 60 BB")
    # sleep(3)
    # print("Zoom level: ", cam.getZoomLevel())

    # cam.requestZoomLevel(1)
    # sleep(3)
    # print("Zoom level: ", cam.getZoomLevel())

    # cam.requestZoomOut()
    # sleep(3)
    # cam.requestZoomHold()
    # sleep(1)
    # print("Zoom level: ", cam.getZoomLevel())
    # cam.requestZoomLevel(1)
    # cam.requestZoomHold()
    # print("Zoom level: ", cam.getZoomLevel())
    # sleep(4)
    # cam.requestZoomLevel(4.5)
    # cam.requestZoomHold()
    # print("Zoom level: ", cam.getZoomLevel())
    # sleep(4)
    # cam.requestZoomLevel(30)
    # cam.requestZoomHold()
    # print("Zoom level: ", cam.getZoomLevel())
    # sleep(4)
    # cam.requestZoomLevel(1)
    # cam.requestZoomHold()
    # print("Zoom level: ", cam.getZoomLevel())
    # val = cam.requestZoomIn()
    # sleep(1)
    # val = cam.requestZoomHold()
    # sleep(1)
    # print("Zoom level: ", cam.getZoomLevel())
    #
    # val = cam.requestZoomOut()
    # sleep(1)
    # val = cam.requestZoomHold()
    # sleep(1)
    # print("Zoom level: ", cam.getZoomLevel())

    cam.disconnect()


if __name__ == "__main__":
    test()
