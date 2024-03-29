import cv2

stage = cv2.imread("Python/pygame._project/ballon1.png",cv2.IMREAD_COLOR)
weapon = cv2.imread("Python/pygame._project/weapon.png",cv2.IMREAD_GRAYSCALE)
ballon1 = cv2.imread("Python/pygame._project/ballon1.png",cv2.IMREAD_COLOR)

cv2.imshow("Python/pygame._project/ballon1.png",stage)
cv2.imshow("Python/pygame._project/weapon.png",weapon)
cv2.imshow("Python/pygame._project/ballon1.png",ballon1)
cv2.waitKey()