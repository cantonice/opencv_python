import cv2

image = cv2.imread(filename="plane.jpg")

gauss_0 = cv2.GaussianBlur(src=image, ksize=(5, 5), sigmaX=0)
gauss_1 = cv2.GaussianBlur(src=image, ksize=(3, 3), sigmaX=0)

median_0 = cv2.medianBlur(src=image, ksize=5)
median_1 = cv2.medianBlur(src=image, ksize=3)

cv2.imshow(winname="image", mat=image)
cv2.imshow(winname="gauss_0", mat=gauss_0)
cv2.imshow(winname="gauss_1", mat=gauss_1)
cv2.imshow(winname="median_0", mat=median_0)
cv2.imshow(winname="median_1", mat=median_1)

cv2.waitKey()


