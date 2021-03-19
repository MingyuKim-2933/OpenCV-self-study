'''
04 히스토그램 분석

히스토그램(Histogram)
- 영상의 픽셀 값 분포를 그래프의 형태로 표현한 것
- 예를 들어 그레이스케일 영상에서 각 그레이스케일 값에 해당하는 픽셀의 개수를 구하고, 이를 막대 그래프의 형태로 표현

정규화된 히스토그램(Normalized histogram)
- 각 픽셀의 개수를 영상 전체 픽셀 개수로 나누어준 것
- 해당 그레이스케일 값을 갖는 픽셀이 나타날 확률

히스토그램 구하기
cv2.calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None) -> hist
- images: 입력 영상 리스트 (1개의 영상이라도 리스트로 묶어서 입력 값으로 주어야한다.)
- channels: 히스토그램을 구할 채널을 나타내는 리스트
- mask: 마스크 영상. 입력 영상 전체에서 히스토그램을 구하려면 None 지정.
- histSize: 히스토그램 각 차원의 크기(빈(bin)의 개수)를 나타내는 리스트
- ranges: 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
- hist: 계산된 히스토그램 (numpy.ndarray 형태로 반환된다.)
- accumulate: 기존의 hist 히스토그램에 누적하려면 True, 새로 만들려면 False.
'''

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


# 그레이스케일 영상의 히스토그램
def show_gray_hist():
    src = cv2.imread('img/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    hist = cv2.calcHist([src], [0], None, [256], [0, 256])  # 이미지를 list로 묶어서 준다. GrayScale은 채널이 0, mask는 None
    # histSize(bin의 개수)는 256, ranges는 0부터 256으로 주었다.

    cv2.imshow('src', src)
    plt.plot(hist)
    plt.show()

    cv2.destroyAllWindows()


# 컬러 영상의 히스토그램
def show_color_hist():
    src = cv2.imread('img/lenna.bmp')

    if src is None:
        print('Image load failed!')
        sys.exit()

    colors = ['b', 'g', 'r']
    bgr_planes = cv2.split(src)

    for (p, c) in zip(bgr_planes, colors):
        hist = cv2.calcHist([p], [0], None, [256], [0, 256])  # 이미지를 list로 묶어서 준다. GrayScale은 채널이 0, mask는 None
        # histSize(bin의 개수)는 256, ranges는 0부터 256으로 주었다.
        plt.plot(hist, color=c)

    cv2.imshow('src', src)
    plt.show()

    cv2.destroyAllWindows()

# OpenCV 그리기 함수로 그레이스케일 영상의 히스토그램 나타내기
def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

# OpenCV 그리기 함수로 히스토그램 출력
def OpenCV_drawing_hist():
    src = cv2.imread('img/lenna.bmp',cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    hist = cv2.calcHist([src], [0], None, [256], [0,256])
    histImg = getGrayHistImage(hist)

    cv2.imshow('histImg', histImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

show_gray_hist()
show_color_hist()
OpenCV_drawing_hist()

