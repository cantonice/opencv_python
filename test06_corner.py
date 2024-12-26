# 图像特征的提取
import cv2

image = cv2.imread("opencv_logo.jpg")

gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

# 获取图像中的特征点
corners = cv2.goodFeaturesToTrack(
    image=gray, maxCorners=500, qualityLevel=0.01, minDistance=10) # 最多返回五百个点，点的质量优于0.1，特征点之间的距离大于10
# 把每一个点标记出来
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img=image, center=(int(x), int(y)), radius=3, color=(255, 0, 255), thickness=-1)

cv2.imshow("corners", image)
cv2.imshow("gray", gray)
cv2.waitKey(0)