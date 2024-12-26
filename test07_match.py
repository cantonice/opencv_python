import cv2
import numpy as np

image = cv2.imread("poker.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

template = gray[75:105, 235:265]

cv2.imshow("template", template)

match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED) # 标准相关匹配算法，标准化再做匹配

# 返回的是一个元组，其中包含两个数组：第一个数组是匹配位置的 y 坐标（行索引），第二个数组是 x 坐标（列索引）。
location = np.where(match>0.9)
print(location)
print(*location)
print(*location[::-1])

# 把模板图案的长和宽求出来
w, h = template.shape[0:2]
for p in zip(*location[::-1]):
    x1, y1 = p[0], p[1]
    x2, y2 = p[0]+w, p[1]+h
    cv2.rectangle(img=image, pt1=(x1,y1), pt2=(x2,y2), color=(0, 255, 0), thickness=2)

cv2.imshow("image", image)

cv2.waitKey()