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
    print("Current Zoom Level is: ", cam.getZoomLevel())

    print('Requesting Absolute Zoom Level 2 and waiting for 4 seconds')
    cam.requestZoomLevel(2)
    sleep(4)
    cam.requestZoomHold()
    sleep(1)
    print("Getting Current Zoom Level: ", cam.getZoomLevel())

    print('Requesting Absolute Zoom Level 1 and waiting for 7 seconds')
    cam.requestZoomLevel(1)
    sleep(7)
    cam.requestZoomHold()
    sleep(1)
    print("Expected Zoom Level to be 1, Actual Zoom Level: ", cam.getZoomLevel())
    print("Requesting Zoom out for 3 seconds. Ideally should not zoom out as we already reached the minimum zoom level")
    cam.requestZoomOut()
    sleep(3)
    print("Gettings current Zoom Level: ", cam.getZoomLevel())

if __name__ == "__main__":
    test()
