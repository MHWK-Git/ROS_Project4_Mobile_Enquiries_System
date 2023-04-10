#!/usr/bin/python3

import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Bool


class CallButton(Node):
    def __init__(self):
        super().__init__('Library_Talker_node')
        self.button_pub = self.create_publisher(Bool, 'button_state', 10)
        self.timer = self.create_timer(0.5, self.button_callback)
        self.get_logger().info("Node CallButton started")

    def button_callback(channel):
        if (GPIO.input(17) == False):
            msg = Bool()
            msg.data = True
            channel.button_pub.publish(msg)
            channel.get_logger().info("Button pressed")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(17, GPIO.RISING, callback=button_callback)


def main(args=None):
    rclpy.init(args=args)
    node = CallButton()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown


if __name__ == '__main__':
    main()
