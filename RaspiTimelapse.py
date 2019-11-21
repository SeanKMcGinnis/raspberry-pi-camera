import time
import picamera

#########################################################################################
## Capture Images with Picamera
## delay            - REQUIRED - time delay in minutes to start taking pictures after initializing
## flight_duration  - REQUIRED - estimated length of flight in minutes
## image_interval   - REQUIRED - delay betwen pictures in seconds
#########################################################################################

def captureImages(delay, flight_duration, image_interval):

    camera = picamera.PiCamera()
    true_interval = image_interval - 3
    image_count = (flight_duration * 60)/image_interval
    print 'Going to Capture %s images over %s minutes with %s seconds between images' % (image_count, flight_duration, image_interval)
    time.sleep(delay)
    try:
        for x in range(image_count):
            timestr = time.strftime("%Y%m%d-%H%M%S")
            camera.capture('ImageOutput/img_' + timestr +'.jpg')
            time.sleep(true_interval)
    finally:
        camera.close()
        print 'Image capture session ended'
