#references: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/
# lab 1 task 4.3

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # color is #ff0000, rgb(255,0,,0), hsl( 0, 100%, 80%)
    # HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    color_lower_hsv = np.array([0, 235, 235], np.uint8)
    color_upper_hsv = np.array([10, 255, 255], np.uint8)
    color_mask_hsv = cv2.inRange(hsv, color_lower_hsv, color_upper_hsv)

    kernal = np.ones((5, 5), "uint8")

    color_mask_hsv = cv2.dilate(color_mask_hsv, kernal)
    res_color = cv2.bitwise_and(hsv, hsv,
                               mask = color_mask_hsv)

    contours, hierarchy = cv2.findContours(color_mask_hsv,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(hsv, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('frame_hsv', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
