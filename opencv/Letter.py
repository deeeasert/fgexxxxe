import numpy as np, cv2

Letter = cv2.imread("S:/Letter.png", cv2.IMREAD_GRAYSCALE)
if Letter is None:
    raise Exception("읽기 오류")

dst = cv2.Canny(Letter, 50, 200)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()