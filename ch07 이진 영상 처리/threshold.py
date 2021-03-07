'''
01 영상의 이진화

영상의 이진화(Binarization)란?
- 영상의 픽셀 값을 0 또는 255(1)로 만드는 연산 (e.g. 배경(background) vs. 객체(object), 관심 영역 vs. 비관심 영역)

그레이스케일 영상의 이진화
g(x, y) = 0 if f(x, y) <= T, 255 if f(x,y) > T
T: 임계값, 문턱치, threshold

임계값 함수
cv2.threshold(src, thresh, maxval, type, dst=None) -> retval, dst
- src: 입력 영상. 다채널, 8비트 또는 32비트 실수형.
- thresh: 사용자 지정 임계값
- maxval: cv2.THRESH_BINARY 또는 cv2.THRESH_BINARY_INV 방법(두 가지 방법이 가장 많이 쓰인다.) 사용 시 최댓값. 보통 255로 지정.
- type: cv2.THRESH_ 로 시작하는 플래그. 임계값 함수 동작 지정 또는 자동 임계값 결정 방법 지정
- retval: 사용된 임계값
- dst: 출력 영상. src와 동일 크기, 동일 타입, 같은 채널 수.
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/cells.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


def threshold1():
    _, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)  # 첫번째 값에 _를 넣어줘야 원하는 결과를 얻을 수 있다.
    _, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()


def threshold2():  # trackbar를 사용하여 threshold를 지정할 수 있다.
    def on_threshold(pos):
        _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
        cv2.imshow('dst', dst)

    cv2.imshow('src', src)
    cv2.namedWindow('dst')
    cv2.createTrackbar('Threshold', 'dst', 0, 255, on_threshold)
    cv2.setTrackbarPos('Threshold', 'dst', 128)

    cv2.waitKey()
    cv2.destroyAllWindows()


threshold1()
threshold2()

