from SimpleCV import Camera

# Initialize the camera
cam = Camera()

# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()
    # Make image black and white
    #img = img.binarize() // Shits broke yo

    # Process the image
    # use a keypoint detector to find areas of interest
    feats = img.findKeypoints()
    # draw the list of keypoints
    feats.draw(color=Color.RED)
    # apply the stuff we found to the image.
    output = img.applyLayers()

    # Save the image(s)
    img.save("img.png")
    output.save("img_keypoints.png")
