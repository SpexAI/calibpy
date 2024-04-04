import sys
# enforce opencv 4.7 over 4.9 on latest systems
if sys.version_info >= (3,12,2):
    # this is the path opencv-python installs into (when built from source)
    sys.path.insert(0,'/usr/local/lib/python3.12/site-packages')
