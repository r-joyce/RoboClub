#!/usr/bin/ python
import SimpleCV

# Initialize the camera
cam = Camera()

# Initialize the template image
template = Image("template.bmp")

# Extract the yellow
temp_yellow = template.colorDistance(Color.YELLOW)
temp_yellow.save("temp_yellow.png") # TODO: Remove
only_yellow = template - temp_yellow
only_yellow.save("only_yellow.png") # TODO: Remove

# Get the mean colors of the template image
template_mean_colors = only_yellow.meanColor()

# Get image from the camera
img = cam.getImage()

# Loop to continuously get images from the camera
while True:
    # Get image from camera
    img = cam.getImage()

    # Extract the yellow
    img_yellow = img.colorDistance(Color.YELLOW)
    img_only_yellow = img - img_yellow

    # Get the mean colors of the current image
    img_mean_colors = img_only_yellow.meanColor()

    # Compare the images
    # pseudo:
    # if R > ??? and G > ??? and B > ???:
    #    we can see the F!
    #    break and start the landing script

# Save the image(s)
img.save("img.png")


# - keypoint Stuff -
# Process the image
# use a keypoint detector to find areas of interest
#feats = img.findKeypoints()
# draw the list of keypoints
#feats.draw(color=Color.RED)
# apply the stuff we found to the image.
#output = img.applyLayers()
