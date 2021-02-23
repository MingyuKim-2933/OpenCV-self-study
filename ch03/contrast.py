'''
05 영상의 명암비 조절

명암비(Contrast)란?
- 밝은 곳과 어두운 곳 사이에 드러나는 밝기 정도의 차이
- 컨트라스트, 대비
- 명암비가 높으면 밝은 부분과 어두운 부분의 픽셀 값의 차이가 커서 조금 더 선명해보인다.

기본적인 명암비 조절 함수
dst(x, y) = saturate(s·src(x, y))
- s = 0.5인 경우 : 최대 픽셀 값이 128이라 전체적으로 어두워 진다.
- s = 2인 경우 : 전체적으로 255가 되는 부분이 많아서 하얗게 보이는 부분이 많다.

효과적인 명암비 조절 함수
dst(x, y) = saturate(src(x, y) + (src(x, y) - 128)·α)
(1 + α) * src(x, y) - 128 * α  # 위의 식과 같다.

히스토그램 스트레칭(Histogram stretching)
- 영상의 히스토그램이 그레이스케일 전 구간에서 걸쳐 나타나도록 변경하는 선형 변환 기법 (양쪽으로 늘려주는 과정에서 중간 중간 픽셀 값이 없는 구간이 생긴다.)

정규화 함수
cv2.normalize(src, dst, alpha=None, beta, None, norm_type=None, dtype=None, mask=None) -> dst
- src: 입력 영상
- dst: 결과 영상 (스트레칭에서는 None 값으로 주면 된다.)
- alpha: (노름 정규화인 경우) 목표 노름 값, (원소 값 범위 정규화인 경우) 최솟값
- beta: (원소 값 범위 정규화인 경우) 최댓값
- norm_type: 정규화 타입. NORM_INF, NORM_L1, NORM_L2, NORM_MINMAX.  # NORM_MINMAX를 선택한 후 alpha에 0 beta에 255를 대입한다.
- dtype: 결과 영상의 타입
- mask: 마스크 영상

히스토그램 스트레칭 변환 함수
(f(x, y) -G(min)) / (G(max) - G(min)) * 255  # 변환 함수의 직선의 방정식
'''

import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist


def contrast1():
    src = cv2.imread('img/lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    alpha = 1.0

    # np.clip을 활용해 0과 255 사이의 값으로 제한하고 astype()을 사용해 float형에서 uint8로 변경한다.
    dst = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)

    cv2.imshow('src1', src)
    cv2.imshow('dst1', dst)
    cv2.waitKey()

    cv2.destroyAllWindows()


def contrast2():
    src = cv2.imread('img/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)  # src가 만약 실수로 저장되어 있으면 dtype=np.uint8을 지정해야 한다.

    # numpy 라이브러리를 사용하여 직접 정규화한다. 위의 결과(dst)와 같다.
    gmin = np.min(src)
    gmax = np.max(src)
    dst2 = np.clip((src - gmin) / (gmax - gmin) * 255., 0, 255).astype(np.uint8)

    hist = cv2.calcHist([src], [0], None, [256], [0,256])
    histImg = getGrayHistImage(hist)

    hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
    histImg2 = getGrayHistImage(hist2)

    hist3 = cv2.calcHist([dst2], [0], None, [256], [0, 256])
    histImg3 = getGrayHistImage(hist3)



    cv2.imshow('src2', src)
    cv2.imshow('dst2', dst)
    cv2.imshow('histImg', histImg)
    cv2.imshow('histImg2', histImg2)
    cv2.imshow('histImg3', histImg3)
    cv2.waitKey()

    cv2.destroyAllWindows()

contrast1()
contrast2()

