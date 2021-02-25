'''
07 특정 색상 영역 추출

RGB 색 공간에서 특정 색상 영역을 추출하기 보다 HSV, YCrCb 공간에서 특정 색상 영역 추출을 많이한다.

HSV 색 공간에서 녹색 영역 추출하기
- H(Hue): 색상의 종류 (색상) (0 ~ 179)
- S(Saturation): 색상의 채도 (선명도) (0 ~ 255) (어느정도 값을 높게 설정해야한다. ex.150 < S < 255)
- V(Value): 색상의 명도 (밝기) (0 ~ 255)

특정 범위 안에 있는 행렬 원소 검출
cv2.inRange(src, lowerb, upperb, dst=None) -> dst (mask 영상: 0 또는 255로만 구성된 이진 영상)
- src: 입력 행렬
- lowerb: 하한 값 행렬 또는 스칼라
- upperb: 상한 값 행렬 또는 스칼라
- dst: 입력 영상과 같은 크기의 마스크 영상. 범위 안에 들어가는 픽셀은 255, 나머지는 0으로 설정. (numpy.uint8)
'''
import sys
import numpy as np
import cv2


def on_trackbar(pos):
    src = cv2.imread('img/candies.png')  # 밝은 캔디 영상
    if src is None:
        print('Image load failed!')
        sys.exit()

    src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')

    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    cv2.imshow('dst', dst)


# BGR 색 공간, HSV 색 공간에서 색상 추출하기
def in_range1():

    src = cv2.imread('img/candies.png')  # 밝은 캔디 영상
    # src = cv2.imread('img/candies2.png')  # 조금 더 어두운 캔디 영상 (BGR 영상에서 추출하면 잘 되지 않는다.)

    if src is None:
        print('Image load failed!')
        sys.exit()

    src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))  # BGR 영상에서 Green 검출
    dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))  # HSV 형식에서 Green(50~80) 검출

    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)

    cv2.waitKey()
    cv2.destroyAllWindows()


# Trackbar를 이용한 특정 색상 영역 추출
def in_range2():
    src = cv2.imread('img/candies.png')  # 밝은 캔디 영상
    if src is None:
        print('Image load failed!')
        sys.exit()

    cv2.imshow('src', src)
    cv2.namedWindow('dst')

    cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar)
    cv2.createTrackbar('H_max', 'dst', 50, 179, on_trackbar)
    on_trackbar(0)

    cv2.waitKey()
    cv2.destroyAllWindows()

in_range1()
in_range2()  # Trackbar를 이용한 특정 색상 영역 추출