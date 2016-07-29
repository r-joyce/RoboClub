#!/usr/bin/ python
from SimpleCV import Image

# The BBB on the copter is constantly taking pictures
# The .bat uses pscp to retreive an image over the internal network
# This script should allow for processing of the image gather in order to
# alleviate the cpu load on the BBB

try:
    while True:
        # Grab an image
        

        # Process the image

except KeyboardInterrupt:
    pass
