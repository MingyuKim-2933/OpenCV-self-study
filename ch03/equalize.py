'''
06 히스토그램 평활화

히스토그램 평활화(Histogram equalization)
- 히스토그램이 그레이스케일 전체 구간에서 균일한 분포로 나타나도록 변경하는 명암비 향상 기법
- 히스토그램 균등화, 균일화, 평탄화

히스토그램 평활화를 위한 변환 함수 구하기
- 변환 함수 : dst(x, y) = round(cdf(src(x, y)) * L(max))  # 누적 분포 함수(cdf)를 사용해서 구한다.

히스토그램 평활화
cv2.equalizeHist(src, dst=None) -> dst
- src: 입력 영상. 그레이스케일 영상
- dst: 결과 영상

컬러 히스토그램 평활화
- 직관적 방법: R, G, B 각 색 평면에 대해 히스토그램 평활화
- (입력)컬러 영상 -> (R,G,B) plane 분할 -> 각각 히스토그램 평활화 -> merge -> (출력)컬러 영상  # 이 방법은 색감이 바껴 좋지 않아 이렇게 하면 안된다.
- (입력)컬러 영상 -> (Y,Cr,Cb) plane 분할 -> Y값만 히스토그램 평활화 -> merge -> (출력)컬러 영상  # 색감은 유지되면서 명암비만 증가되어 원하는 결과를 얻을 수 있다.
'''

import sys
import numpy as np
import cv2


def grayscale_equalize():
    src = cv2.imread('img/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    dst = cv2.equalizeHist(src)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


def color_equalize():
    src = cv2.imread('img/field.bmp')

    if src is None:
        print('Image load failed!')
        sys.exit()

    src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    planes = cv2.split(src_ycrcb)

    planes[0] = cv2.equalizeHist(planes[0])  # Y값만 평활화
    dst_ycrcb = cv2.merge(planes)  # YCrCb 이미지이므로 BGR 이미지로 변경해서 출력해야 한다.
    dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()


grayscale_equalize()  # grayscale 히스토그램 평활화
color_equalize()  # color영상 히스토그램 평활화