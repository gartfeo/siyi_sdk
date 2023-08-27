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
    # Problem 2: absolute zoom on 1
    print('Requesting Zoom out for 3 seconds')
    cam.requestZoomOut()
    sleep(3)
    print("Zoom Level: ", cam.getZoomLevel())

    print('Requesting Zoom Level 2')
    cam.requestZoomLevel(2)
    sleep(5)
    cam.requestZoomHold()
    sleep(1)
    print("Zoom Level: ", cam.getZoomLevel())

    print('Requesting Zoom Level 1')
    cam.requestZoomLevel(1)
    sleep(7)
    cam.requestZoomHold()
    sleep(1)
    print("Zoom Level: ", cam.getZoomLevel())
    cam.requestZoomOut()
    sleep(3)
    print("Zoom Level: ", cam.getZoomLevel())

if __name__ == "__main__":
    test()
