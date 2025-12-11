#! /usr/bin/env python
import rospy
import utils
import time

utils.startApplication()


end = time.time() + 30.0
while time.time() < end:
    utils.goStraight(_linear_speed=0.5)
    time.sleep(0.1)  


utils.goStraight(_linear_speed=0.0)
time.sleep(0.2)

rospy.loginfo("limo application end")

