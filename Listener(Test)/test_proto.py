#!/usr/bin/env python3

import tkinter as GUI
from tkinter import *
from PIL import Image, ImageTk
import sys
import select
import os
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import cv2
from GUI_Prog import *
from waypoint import *
if os.name == 'nt':
    import msvcrt
    import time
else:
    import tty
    import termios

# User input when button is pressed once


def getKey():
    if os.name == 'nt':
        timeout = 0.1
        startTime = time.time()
        while (1):
            if msvcrt.kbhit():
                if sys.version_info[0] >= 3:
                    return msvcrt.getch().decode()
                else:
                    return msvcrt.getch()
            elif time.time() - startTime > timeout:
                return ''

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


if __name__ == '__main__':

    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('limo_navigator_node')
    try:
       # User input by getkey to simulate a call button
        print("Please press call button to summon robot")
        while not rospy.is_shutdown():
            key = getKey()
            if key == '1':
                print("Call received")
                Waypoint_Client(0.5, 0.5, 0.0, 1.0)
                rospy.sleep(0.2)
                GUI_func()
                rospy.sleep(10.0)
                break
            elif key == '2':
                print("Call received")
                Waypoint_Client(2.0, 0.1, 0.0, 1.0)
                rospy.sleep(0.2)
                GUI_func()
                rospy.sleep(10.0)
                break
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
