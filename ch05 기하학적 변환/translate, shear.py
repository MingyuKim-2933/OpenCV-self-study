'''
01 영상의 이동 변환과 전단 변환

영상의 기하학적 변환(geometric transformation)이란?
- 영상을 구성하는 픽셀의 배치 구조를 변경함으로써 전체 영상의 모양을 바꾸는 작업
- Image registration, removal of geometric distortion, etc.

이동 변환(Translation transformation)
- 가로 또는 세로 방향으로 영상을 특정 크기만큼 이동시키는 변환
- x축과 y축 방향으로의 이동 변위를 지정
- x' = x+a, y' = y+b

영상의 어파인 변환 함수
cv2.warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None) -> dst
- src: 입력 영상
- M: 2x3 어파인 변환 행렬. 실수형.
- dsize: 결과 영상 크기. (w, h) 튜플. (0, 0)이면 src와 같은 크기로 설정.
- dst: 출력 영상
- flags: 보간법. 기본값은 cv2.INTER_LINEAR.
- borderMode: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT.
- borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.

전단 변환 (Shear transformation)
- 층 밀림 변환. x축과 y축 방향에 대해 따로 정의.
- 평행 사변형 형태로 이동 된다.
- x' = x+my, y' = y and x' = x, y' = mx+y
'''

import sys
import numpy as np
import cv2


def translate():  # 영상의 이동 변환
    src = cv2.imread('img/tekapo.bmp')

    if src is None:
        print('Image load failed!')
        sys.exit()

    aff = np.array([[1, 0, 200], [0, 1, 100]], dtype=np.float32)  # np.array를 만들 때 float 형으로 만들어 줘야한다.
    dst = cv2.warpAffine(src, aff, (0, 0))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def sheer():  # 영상의 전단 변환
    src = cv2.imread('img/tekapo.bmp')

    if src is None:
        print('Image load failed!')
        sys.exit()

    aff = np.array([[1, 0.5, 0], [0, 1, 0]], dtype=np.float32)  # np.array를 float형으로 지정해 줘야 한다.

    h, w = src.shape[:2]
    dst = cv2.warpAffine(src, aff, (w + int(h * 0.5), h))  # 영상의 가로크기를 늘려준다.

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


translate()
sheer()

