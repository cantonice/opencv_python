import cv2

print(cv2.getVersionString())

img = cv2.imread("opencv.jpg")  # numpy数组格式文件
print(img.shape)

cv2.imshow("img",img)  # 第一个img是窗口名（winname），第二个img是变量名，就是上面的numpy变量
cv2.waitKey()  # 让窗口暂停