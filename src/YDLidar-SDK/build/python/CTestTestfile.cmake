# CMake generated Testfile for 
# Source directory: /home/agilex/limo_ws/src/YDLidar-SDK/python
# Build directory: /home/agilex/limo_ws/src/YDLidar-SDK/build/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ydlidar_py_test "/usr/bin/python" "/home/agilex/limo_ws/src/YDLidar-SDK/python/test/pytest.py")
set_tests_properties(ydlidar_py_test PROPERTIES  ENVIRONMENT "PYTHONPATH=/home/agilex/limo_ws/devel/lib/python2.7/dist-packages:/opt/ros/melodic/lib/python2.7/dist-packages:/home/agilex/limo_ws/src/YDLidar-SDK/build/python" _BACKTRACE_TRIPLES "/home/agilex/limo_ws/src/YDLidar-SDK/python/CMakeLists.txt;42;add_test;/home/agilex/limo_ws/src/YDLidar-SDK/python/CMakeLists.txt;0;")
subdirs("examples")
