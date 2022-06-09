import time
import uuid

import cv2

def format_image(image):
    # image如果为彩色图：image.shape[0][1][2](水平、垂直像素、通道数)
    if len(image.shape) > 2 and image.shape[2] == 3:
        # 将图片变为灰度图
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 它可以检测出图片中所有的人脸，并将人脸用vector保存各个人脸的坐标、大小（用矩形表示）
        # 调整scaleFactor参数的大小，可以增加识别的灵敏度，推荐1.1
        #CASC_PATH = 你的haarcascade_frontalface_alt2.xml文件地址
        CASC_PATH = 'E:/miniconda/envs/lstm/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml' #
        cascade_classifier = cv2.CascadeClassifier(CASC_PATH)
        faces = cascade_classifier.detectMultiScale(image, scaleFactor=1.1, minNeighbors=3)
    # 如果图片中没有检测到人脸，则返回None
    if not len(faces) > 0:
        return None, None
    # max_are_face包含了人脸的坐标，大小
    max_are_face = faces[0]
    # 在所有人脸中选一张最大的脸
    for face in faces:
        if face[2] * face[3] > max_are_face[2] * max_are_face[3]:
            max_are_face = face

    # 这两步可有可无
    face_coor = max_are_face
    image = image[face_coor[1]:(face_coor[1] + face_coor[2]), face_coor[0]:(face_coor[0] + face_coor[3])]
    # 调整图片大小，变为48*48
    try:
        image = cv2.resize(image, (48, 48), interpolation=cv2.INTER_CUBIC)
    except Exception:
        print("problem during resize")
        return None, None

    return image, face_coor


def SaveImgTxt(x, y, w, h):
    ImageName = str(uuid.uuid1())
    Speace = " " # 保持空隙
    The_label = "kiven" # 标签的名字
    Xmin = str(x)  # 目标的Xmin
    Ymin = str(y)
    Xmax = str(x + w)
    Ymmax = str(y + h)
    # 写入Txt的内容
    TxtInfo = (ImageName + Speace + The_label + Speace + Xmin + Speace + Ymin + Speace + Xmax + Speace + Ymmax + '\n')
    cv2.imwrite("./face/img/%s.jpg" % ImageName, frame)

    with open("./face/txt/%s.txt" % ImageName, "a", encoding='utf-8') as txt:
        txt.write(TxtInfo)


if __name__ == "__main__":
    capture = cv2.VideoCapture(0)
    fps = 0.0
    while (True):
        t1 = time.time()
        # 读取某一帧
        ref, frame = capture.read()
        # 进行检测
        (p_image, face_coor) = format_image(frame)
        if face_coor is not None:
            # 获取人脸的坐标,并用矩形框出
            [x, y, w, h] = face_coor
            SaveImgTxt(x, y, w, h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

        fps = (fps + (1. / (time.time() - t1)))/2
        frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("video", frame)
        c = cv2.waitKey(1) & 0xff
        if c == 27:
            capture.release()
            break
    capture.release()
    cv2.destroyAllWindows()
