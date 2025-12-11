cmake_minimum_required(VERSION 3.0.2)
project(limo_bringup)

find_package(catkin REQUIRED
  COMPONENTS
    roscpp
    rospy
    tf2_ros
    geometry_msgs
    aruco_ros
)

catkin_install_python(PROGRAMS
  scripts/pose_corrector.py
  DESTINATION \${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_package(
  CATKIN_DEPENDS
    roscpp
    rospy
    tf2_ros
    geometry_msgs
    aruco_ros
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
