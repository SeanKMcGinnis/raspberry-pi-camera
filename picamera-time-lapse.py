import time
import picamera

with picamera.PiCamera() as camera:
    # Open a preview window if you want to see what the camera is capturing
	camera.start_preview()
	# Wait two seconds before capturing images
    time.sleep(2)
	# Create a file name and capture the image
    for filename in camera.capture_continuous('../ImageOutput/img{counter:03d}.jpg'):
        # Write to the console the name of the image captured
		print('Captured %s' % filename)
		#Wait 5 seconds before capturing the next image
        time.sleep(5) # wait 5 seconds
