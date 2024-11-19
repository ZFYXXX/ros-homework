#!/usr/bin/env python3
# coding=utf-8
  

import rospy  
from std_msgs.msg import String  

def callback(data):  
    rospy.loginfo("接收到数据: %s", data.data)  

def listener():  
    rospy.init_node('listener', anonymous=True)  
    rospy.Subscriber("/driver/encoder", String, callback)  
    # rospy.Subscriber("/driver/evl", String, callback)
    # rospy.Subscriber("/driver/imv", String, callback)
    # rospy.Subscriber("/driver/mag", String, callback)
    # rospy.Subscriber("/driver/scan", String, callback)
    rospy.spin()  


if __name__ == '__main__':  
    listener()
