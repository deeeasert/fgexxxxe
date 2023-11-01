import numpy as np, cv2

p1 = cv2.imread("S:/pizza1.png", cv2.IMREAD_COLOR)
p2 = cv2.imread("S:/pizza2.png", cv2.IMREAD_COLOR)
if p1 is None or p2 is None:
    raise Exception("읽기 오류")

img1 = p1[:, :110]
img2 = p2[:, 110:]

img3 = np.concatenate([img1, img2], axis=1)

cv2.imshow("pizza", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()