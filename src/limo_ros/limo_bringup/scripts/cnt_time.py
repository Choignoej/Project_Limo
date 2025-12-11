#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import time
from geometry_msgs.msg import PoseWithCovarianceStamped
# 이부분 메세지 타입을 정확하게 잘 몰라서 gpt 한테 물어봣습니다!!!

from sensor_msgs.msg import LaserScan

class AmclScanDelayNode(object):
    def __init__(self):
       # 노드 초기화
        self.last_scan_time = None
        # 시간을 저정할 변수 선언

        # 평균 시간도 구하면 좋을거 같아서 추가했습니다|

        # 누적 dt
        self.dt_sum = 0.0
        
        # dt 개수
        self.dt_count = 0


        # Subscribers 라이다
        self.scan_sub = rospy.Subscriber("/scan",
                                         LaserScan,
                                         self.scan_callback,
                                         queue_size=1)
        
        # Subscribers amcl
        self.amcl_sub = rospy.Subscriber("/amcl_pose",
                                         PoseWithCovarianceStamped,
                                         self.amcl_callback,
                                         queue_size=1)

    def scan_callback(self, msg): # 라이다 값이 들어온 경우
        # Python 시간(sec) 저장
        self.last_scan_time = time.time() # 라이다 값이 먼저 들어올거니까 last_scan_time에 현재 시간을 저장

    def amcl_callback(self, msg):
        # 현재 시간
        now = time.time() # amcl 토픽이 늦게 들어올거니가 바로 값을 빼기 위해 사용

        if self.last_scan_time is None: # 혹시나 라이다 값이 늦게 들어오면 안대니까.. 
            # 연산 x
            return

        # 시간 차이 계산
        dt = now - self.last_scan_time

        #평균 계산을 위하여 누적 및 카운트 증가
        self.dt_sum += dt
        self.dt_count += 1

          # 평균 계산
        avg_dt = self.dt_sum / self.dt_count

        rospy.loginfo(
            "현재 dt: %.6f초 | 평균 dt: %.6f초 (count=%d)",
            dt, avg_dt, self.dt_count
        )



if __name__ == "__main__":
    rospy.init_node("amcl_scan_delay_node", anonymous=False)
    node = AmclScanDelayNode()
    rospy.spin()
