import cv2

img = cv2.imread("opencv_logo.jpg")

px = img[100, 100]
print(px)

img[100, 100] = [0, 0, 255]
print(img[100, 100])

print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow("modify_pixel", img)

cv2.waitKey(0)
cv2.destroyAllWindows()