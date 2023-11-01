import numpy as np, cv2

image = cv2.imread("S:/Area.bmp", cv2.IMREAD_ANYCOLOR)
if image is None:
    raise Exception("읽기 오류")

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 

lower_blue = (120-10, 30, 30)
upper_blue = (120+10, 255, 255)
img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

img_result = cv2.bitwise_and(image, image, mask = img_mask)


cv2.imshow('image', image)
cv2.imshow('img_mask', img_mask)
cv2.imshow('image', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
