import os
import cv2
import time
import uuid

image_path = 'collected_image'

labels = ['Hello', 'Yes', 'No', 'Thanks', 'I Love You', 'Please']

number_of_images = 20

for label in labels:
    img_path = os.path.join(image_path, label)
    os.makedirs(img_path)
    cap = cv2.VideoCapture(0)
    print(f"Collecting image for {label}")
    time.sleep(5)
    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        imagename = os.path.join(image_path, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()