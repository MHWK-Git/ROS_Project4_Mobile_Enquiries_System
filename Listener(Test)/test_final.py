#!/usr/bin/env python3
import sys
import select
import os
import rospy
from GUI_Prog import *


def callback():
    try:
       # User input by getkey to simulate a call button
        # GUI_func()
        print("Please press call button to summon robot")
        while not rospy.is_shutdown():
            print("Call received")
            Waypoint_Client(2.0, 1.0, 0.0, 1.0)
            rospy.sleep(0.2)
            GUI_func()
            rospy.sleep(5.0)
            break
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")


def listener():
    rospy.init_node('Library_Listener_node', anonymous == False)
    rospy.Subscriber("button_state", Bool, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
