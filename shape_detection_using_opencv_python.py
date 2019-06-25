import numpy as np
import cv2

font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread('/home/ypatel/opencv-master/samples/data/shapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), font, .5, (0))
    elif len(approx) == 4:
        x, y, width, height = cv2.boundingRect(approx)
        aspectRatio = float(width) / height
        print(aspectRatio)

        if aspectRatio >= 0.90 and aspectRatio <= 1.15:
            shape = "square"
            cv2.putText(img, shape, (x, y), font, .5, (0))
        else:
            shape = "rectangle"
            cv2.putText(img, shape, (x, y), font, .5, (0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, .5, (0))
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), font, .5, (0))
    else:
        cv2.putText(img, "Circle", (x, y), font, .5, (0))

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
