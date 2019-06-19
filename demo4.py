import cv2
import numpy as np

cap = cv2.VideoCapture("vtest.avi")

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while ret:

    d = cv2.absdiff(frame1, frame2)

    grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=3)
    cnts, h = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(str(len(cnts)))
        # loop over the contours
    for c in cnts:

        # Save the coordinates of all found contours
        (x, y, w, h) = cv2.boundingRect(c)

        # If the contour is too small, ignore it, otherwise, there's transient
        # movement
        if cv2.contourArea(c) > 700:
            transient_movement_flag = True

            # Draw a rectangle around big enough movements
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #cv2.drawContours(frame1, c, -1, (0, 255, 0), 2)

    cv2.imshow("inter", frame1)

    if cv2.waitKey(40) == 27:
        break
    frame1 = frame2
    ret, frame2 = cap.read()

cv2.destroyAllWindows()
cap.release()
