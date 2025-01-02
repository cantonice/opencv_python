import cv2

# 实例化一个人脸级联分类器对象
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 打开摄像头
capture = cv2.VideoCapture(0)

while True:
    # 读取摄像头每一帧
    ret, frame = capture.read()

    # 将读取到的帧转化为灰度图
    capture_gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    # 使用级联分类器检测人脸，返回的是一个坐标列表，每个坐标是一个(x,y,w,h)的元组
    faces = face_cascade.detectMultiScale(capture_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 读取每一个检测到的目标
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)

    # 显示结果
    cv2.imshow("faces", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
capture.release()

# 关闭所有窗口
cv2.destroyAllWindows()
