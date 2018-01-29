import cv2
import numpy as np
import os


x = "a"

if x == "a":
    print(os.getcwd())
    print(os.listdir())
    # Load an color image in grayscale
    img = cv2.imread('watch.jpg',0)
    #cap = cv2.VideoCapture(0)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
