# 形态学算法
import cv2
import numpy as np

gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)
_, binary_inv = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(binary_inv, kernel)
dilation = cv2.dilate(binary_inv, kernel)

cv2.imshow("binary_inv", binary_inv)
cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)

cv2.waitKey()