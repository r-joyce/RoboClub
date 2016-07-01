#!/usr/bin/ python
from SimpleCV import *

# Initialize the template image
template = Image("red.png")

# Extract the RED
template_red = template.colorDistance(Color.RED)
template_red.save("template_red.png")
only_red = template - template_red
only_red.save("only_red.png")

template_mean_colors = only_red.meanColor()

# use a keypoint detector to find areas of interest
feats = only_red.findKeypoints()
# draw the list of keypoints
feats.draw(color=Color.GREEN)
# apply the stuff we found to the image.
output = feats.applyLayers()

# Save
output.save("output.png")
