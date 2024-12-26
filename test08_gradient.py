import cv2

gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)
gray_1 = cv2.imread("orange.jpg", cv2.IMREAD_GRAYSCALE)
gray_2 = cv2.imread("ic.jpg", cv2.IMREAD_GRAYSCALE)
gray_3 = cv2.imread("keyboard.jpg", cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(src=gray, ddepth=cv2.CV_64F)

canny = cv2.Canny(image=gray, threshold1=100, threshold2=200)
canny_orange = cv2.Canny(image=gray_1, threshold1=100, threshold2=200)
canny_ic = cv2.Canny(image=gray_2, threshold1=100, threshold2=200)
canny_keyboard = cv2.Canny(image=gray_3, threshold1=100, threshold2=200)

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.imshow("canny_orange", canny_orange)
cv2.imshow("canny_ic", canny_ic)
cv2.imshow("canny_keyboard", canny_keyboard)

cv2.waitKey()