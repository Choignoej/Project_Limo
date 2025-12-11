#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from visualization_msgs.msg import Marker
from tf.transformations import quaternion_from_euler

# pose_corrector.py에 있는 '정답' 좌표와 "반드시" 동일해야 합니다.
MARKER_GROUND_TRUTH = {
    0: {'x': -2.64652490616, 'y': -0.778705239296, 'yaw': 3.1415}, # 0번 마커
    1: {'x': -0.52717846632, 'y': 0.940190792084, 'yaw': -1.5708}, # 1번 마커
    2: {'x': 2.01360464096, 'y': -0.450913339853, 'yaw': 3.1415}, # 2번 마커
    3: {'x': 3.34300923347, 'y': 1.87512040138, 'yaw': -1.5708}  # 3번 마커
}

rospy.init_node('ground_truth_visualizer')

# Rviz의 Marker 설정과 동일한 토픽 (visualization_marker)
pub_marker = rospy.Publisher('/visualization_marker', Marker, queue_size=10)

# 1초에 한 번씩 마커를 계속 발행 (Rviz가 껐다 켜져도 볼 수 있게)
rate = rospy.Rate(1) 

rospy.loginfo("Ground truth 마커 발행 시작...")

while not rospy.is_shutdown():
    
    for marker_id, info in MARKER_GROUND_TRUTH.items():
        marker = Marker()
        
        # Rviz의 'Fixed Frame' (map)과 일치해야 함
        marker.header.frame_id = "map" 
        marker.header.stamp = rospy.Time.now()
        
        marker.ns = "ground_truth_markers" # 마커 그룹 이름
        marker.id = marker_id
        
        marker.type = Marker.ARROW # 화살표 모양
        marker.action = Marker.ADD
        
        # 마커 위치 및 방향 설정
        marker.pose.position.x = info['x']
        marker.pose.position.y = info['y']
        marker.pose.position.z = 0.0
        
        q = quaternion_from_euler(0, 0, info['yaw'])
        marker.pose.orientation.x = q[0]
        marker.pose.orientation.y = q[1]
        marker.pose.orientation.z = q[2]
        marker.pose.orientation.w = q[3]

        # 마커 크기 (화살표 길이 0.5m, 두께 0.05m)
        marker.scale.x = 0.5
        marker.scale.y = 0.05
        marker.scale.z = 0.05

        # 마커 색상 (빨간색, 불투명)
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0 # (중요!) 0.0이면 투명해서 안 보입니다.

        # 마커 유지 시간 (rate가 1Hz이므로 1.5초로 넉넉하게 설정)
        marker.lifetime = rospy.Duration(1.5)

        # 마커 발행
        pub_marker.publish(marker)

    rate.sleep()
