import csv
import time
import picamera
from datetime import datetime

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
    csv_filename = datetime.now().strftime("%m_%d_%Y") + "_images.csv"
    with open(csv_filename, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
        # To extend the information collected, edit the row below to include the desired field headers
        filewriter.writerow(['photo', 'lat', 'long', 'date'])
        print 'Going to Capture %s images over %s minutes with %s seconds between images' % (image_count, flight_duration, image_interval)
        time.sleep(delay)
        try:
            for x in range(image_count):
                timestr = time.strftime("%Y%m%d-%H%M%S")
                img_filename = 'ImageOutput/img_' + timestr +'.jpg'
                camera.capture(img_filename)
                # Include the additional attributes in the row below if desired
                filewriter.writerow([img_filename, '77.062', '33.872', timestr])
                time.sleep(true_interval)
        finally:
            camera.close()
            csvfile.close()
            print 'Image capture session ended'
