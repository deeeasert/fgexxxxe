import numpy as np, cv2

text = cv2.imread("S:/CharExtraction.bmp", cv2.IMREAD_COLOR)
if text is None:
    raise Exception("읽기 오류")

text_hsv = cv2.cvtColor(text, cv2.COLOR_BGR2HSV) 

lower_green = (30, 30, 30)
upper_green = (90, 255, 255)
text_mask = cv2.inRange(text_hsv, lower_green, upper_green)

img_result = cv2.bitwise_and(text, text, mask = text_mask)

cv2.imshow('text', text)
cv2.imshow('text_mask', text_mask)
cv2.imshow('image', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
