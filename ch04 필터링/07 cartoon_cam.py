'''
07 카툰 필터 카메라

카툰 필터 카메라
- 카메라 입력 영상에 실시간으로 재미있는 필터링을 적용하는 기능

구현 할 기능
- 카툰 필터
- 스케치 필터
- 스페이스바를 누를 때마다 모드 변경

카툰 필터
- 입력 영상의 색상을 단순화시키고, 에지 부분을 검정색으로 강조

스케치 필터
- 평탄한 영역은 흰색
- 에지 근방에서 어두운 영역을
검정색으로 설정. (밝은 영역은 흰색)
'''

import sys
import numpy as np
import cv2


def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))  # 축소한 후 컬러 단순화를 하면 효과가 더 좋다.

    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)  # 아직 GrayScale 영상
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)  # INTER_NEAREST를 주면 더 카툰스러운 모습을 나타낼 수 있다.

    return dst


def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0, 0), 3)
    dst = cv2.divide(gray, blr, scale=255)

    return dst


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('video open failed!')
    sys.exit()

cam_mode = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0


cap.release()
cv2.destroyAllWindows()
