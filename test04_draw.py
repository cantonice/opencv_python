import cv2
import numpy as np

image = np.zeros([300, 300, 3], dtype=np.uint8)

cv2.line(img=image, pt1=(100,200), pt2=(250,250), color=(255, 0, 0), thickness=2)
cv2.rectangle(img=image, pt1=(30, 100), pt2=(60,150), color=(0, 255, 0), thickness=2)
cv2.circle(img=image, center=(150, 100), radius=60, color=(0, 0, 255), thickness=2)
cv2.putText(img=image,text="hello world!", org=(100, 50), fontFace=0, fontScale=1, color=(100,100,100), thickness=2, lineType=1)

cv2.imshow("image", image)
cv2.waitKey(0)