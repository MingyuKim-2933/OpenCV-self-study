'''
08 히스토그램 역투영

히스토그램 역투영(Histogram backprojection)
- 영상의 각 픽셀이 주어진 히스토그램 모델에 얼마나 일치하는지를 검사하는 방법
- 임의의 색상 영역을 검출할 때 효과적(inrange 함수보다 임의의 색상 영역을 검출한다. e.x. 살색)
- YCrCb 컬러 스페이스와 LAB를 많이 쓴다.

히스토그램 역투영을 이용한 살색 검출
1) 기준 영상으로부터 살색에 대한 컬러 히스토그램을 미리 계산
2) 입력 영상에서 미리 구한 살색 히스토그램에 부합하는 픽셀을 선별

히스토그램 역투영 함수
cv2.calcBackProject(images, channels, hist, ranges, scale, dst=None) -> dst
- images: 입력 영상 리스트
- channels: 역투영 계산에 사용할 채널 번호 리스트
- hist: 입력 히스토그램(numpy.ndarray)
- ranges: 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
- scale: 출력 역투영 행렬에 추가적으로 곱할 값
- dst: 출력 역투영 영상. 입력 영상과 동일 크기, cv2.CV_8U.
'''

import sys
import numpy as np
import cv2

def backproj1():
    # 입력 영상에서 ROI를 지정하고, 히스토그램 계산
    src = cv2.imread('img/cropland.png')

    if src is None:
        print('Image load failed!')
        sys.exit()

    x, y, w, h = cv2.selectROI(src)  # 마우스로 드래그해서 ROI를 지정한다.

    src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    crop = src_ycrcb[y:y+h, x:x+w]  # 사용자가 선택한 사각형 영역의 부분 영상

    # 히스토그램을 계산해주는 코드
    channels = [1, 2]  # 0번 채널을 사용하지 않으면 밝기에 영향을 덜 받는다.
    cr_bins = 128
    cb_bins = 128
    histSize = [cr_bins, cb_bins]
    cr_range = [0, 256]
    cb_range = [0, 256]
    ranges = cr_range + cb_range

    hist = cv2.calcHist([crop], channels, None, histSize, ranges)
    hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # 입력 영상 전체에 대해 히스토그램 역투영
    backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)  # 원하는 색상 영역만 추출한다.
    dst = cv2.copyTo(src, backproj)

    cv2.imshow('backproj', backproj)
    cv2.imshow('hist_norm', hist_norm)
    cv2.imshow('dst', dst)

    cv2.waitKey()
    cv2.destroyAllWindows()

def backproj2():
    # CrCb 살색 히스토그램 구하기
    ref = cv2.imread('img/kids1.png', cv2.IMREAD_COLOR)
    mask = cv2.imread('img/kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)

    if ref is None or mask is None:
        print('Image load failed!')
        sys.exit()

    ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

    channels = [1, 2]  # 0번 채널을 사용하지 않으면 밝기에 영향을 덜 받는다.
    ranges = [0, 256, 0, 256]
    hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)
    hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)  # logscale로 출력하면 좋다.

    # 입력 영상에 히스토그램 역투영 적용
    src = cv2.imread('img/kids2.png', cv2.IMREAD_COLOR)
    if src is None:
        print('Image load failed!')
        sys.exit()

    src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

    backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)  # 원하는 색상 영역만 추출한다.

    cv2.imshow('src', src)
    cv2.imshow('hist_norm', hist_norm)
    cv2.imshow('backproj', backproj)

    cv2.waitKey()
    cv2.destroyAllWindows()

backproj2()