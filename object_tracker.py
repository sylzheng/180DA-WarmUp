#references: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/
# modified to use an rgb color mask in addition to hsv
# lab 1 task 4.1 and 4.2

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue_lower_hsv = np.array([90, 75, 5], np.uint8)
    blue_upper_hsv = np.array([120, 255, 255], np.uint8)
    blue_mask_hsv = cv2.inRange(hsv, blue_lower_hsv, blue_upper_hsv)

    kernal = np.ones((5, 5), "uint8")

    blue_mask_hsv = cv2.dilate(blue_mask_hsv, kernal)
    res_blue = cv2.bitwise_and(hsv, hsv,
                               mask = blue_mask_hsv)

    contours, hierarchy = cv2.findContours(blue_mask_hsv,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(hsv, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
    
    # RGB
    blue_lower_rgb = np.array([50, 0, 0], np.uint8)
    blue_upper_rgb = np.array([255, 120, 120], np.uint8)
    blue_mask_rgb = cv2.inRange(frame, blue_lower_rgb, blue_upper_rgb)

    blue_mask_rgb = cv2.dilate(blue_mask_rgb, kernal)
    res_blue = cv2.bitwise_and(frame, frame,
                               mask = blue_mask_rgb)

    contours, hierarchy = cv2.findContours(blue_mask_rgb,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
    # Display the resulting frame
    cv2.imshow('frame_rdb', frame)
    cv2.imshow('frame_hsv', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
