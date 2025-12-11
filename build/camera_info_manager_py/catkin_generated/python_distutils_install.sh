#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/agilex/limo_ws/src/src/camera_info_manager_py"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/agilex/limo_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/agilex/limo_ws/install/lib/python2.7/dist-packages:/home/agilex/limo_ws/build/camera_info_manager_py/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/agilex/limo_ws/build/camera_info_manager_py" \
    "/usr/bin/python2" \
    "/home/agilex/limo_ws/src/src/camera_info_manager_py/setup.py" \
     \
    build --build-base "/home/agilex/limo_ws/build/camera_info_manager_py" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/agilex/limo_ws/install" --install-scripts="/home/agilex/limo_ws/install/bin"
