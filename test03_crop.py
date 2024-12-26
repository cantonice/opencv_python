import cv2

img = cv2.imread("opencv.jpg")

crop = img[100:473, 10:200]

# cv2.imshow("img",img)
cv2.imshow("crop",crop)

cv2.waitKey()