import csv
import time
import picamera
from datetime import dateime

#########################################################################################
## Capture Images with Picamera
## delay            - REQUIRED - time delay in minutes to start taking pictures after initializing
## flight_duration  - REQUIRED - estimated length of flight in minutes
## image_interval   - REQUIRED - delay betwen pictures in seconds
## create_csv     - REQUIRED - save the record for ArcGIS Online
#########################################################################################

def captureImages(delay, flight_duration, image_interval, create_csv):
    camera = picamera.PiCamera()
    true_interval = image_interval - 3
    image_count = (flight_duration * 60)/image_interval
    if create_csv:
        csv_filename = datetime.now().strftime("%m_%d_%Y") + "_images.csv"
        with open(csv_filename, 'wb') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',', quotechar="|", quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['photo', 'lat', 'long', 'date'])
    print 'Going to Capture %s images over %s minutes with %s seconds between images' % (image_count, flight_duration, image_interval)
    time.sleep(delay)
    try:
        for x in range(image_count):
            timestr = time.strftime("%Y%m%d-%H%M%S")
            img_filename = 'ImageOutput/img_' + timestr +'.jpg'
            camera.capture(img_filename)
            if create_csv:
                filewriter.writerow([img_filename, '77.062', '33.872', timestr])
            time.sleep(true_interval)
    finally:
        camera.close()
        if create_csv:
            csvfile.close()
        print 'Image capture session ended'
