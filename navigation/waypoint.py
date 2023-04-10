#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# function to go to a specific waypoint
def Waypoint_Client(x_pos, y_pos, z_ori, w_ori):
    
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map' 
    # Move x_pos meters forward along the x axis of the "map" 
    # Move y_pos meters down along the y axis of the "map" 
    goal.target_pose.pose.position.x = x_pos
    goal.target_pose.pose.position.y = y_pos
    # Quaternion values to face a different direction
    goal.target_pose.pose.orientation.z = z_ori
    goal.target_pose.pose.orientation.w = w_ori

    client.send_goal(goal)
    wait = client.wait_for_result()

    rospy.sleep(0.5)

   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

