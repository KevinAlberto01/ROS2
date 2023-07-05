#!/usr/bin/env python3
#the fisrt line is a interpretive line, because ros2 only use python3 
import rclpy #library for python that ros2 use 
from rclpy.node import Node #node class for create a node 

def main(args=None): #fuction name with opcional arguments,  
    rclpy.init(args=args) #initializate the ros2 communication
    node = Node("py_test") #its the node with the name 
    node.get_logger().info("Hello ROS2") #its to print
    rclpy.spin(node) #will oppose the program and allow you node continue to be alive help to the callbacks
    rclpy.shutdown() #its the las line of comminication

if __name__ == "__main__": #structure 
    main() 

