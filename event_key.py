import numpy as np
import cv2

switch_case = {
    ord('a'): "a키",
    ord('b'): "b키",
    0x41: "A키",
    int('0x42', 16): "B키 입력",
    2424832: "왼쪽 화살표키",
    2490368: "위쪽 화살표키",
    2555904: "오른쪽 화살표키",
    2621440: "아래쪽 화살표키"
}

image = np.ones((200, 300), np.float32)
cv2.namedWindow('Keyboard Event')
cv2.imshow("Keyboard Event", image)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()

#branch test
#main test2
#cv1