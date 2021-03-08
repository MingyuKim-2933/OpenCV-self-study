'''
03 지역 이진화

균일하지 않은 조명 환경에서 촬영된 영상의 이진화
- threshold2.py 프로그램에 sudoku.jpg 파일을 입력으로 사용

균일하지 않은 조명의 영향을 해결하려면?
- 불균일한 조명 성분을 보상한 후 전역 이진화 수행

Surface Fitting -> Shading Compensation(이미지 전체가 균일하게 조명을 받도록 보정) -> Global Thresholding

균일하지 않은 조명의 영향을 해결하려면?
- 픽셀 주변에 작은 윈도우를 설정하여 지역 이진화 수행
  - 윈도우의 크기는?
  - 윈도우 형태는? Uniform? Gaussian?
  - 윈도우를 겹칠 것인가? Overlap? Non-overlap?
  - 윈도우 안에 배경 또는 객체만 존재한다면?

OpenCV 적응형 이진화
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None) -> dst
- src: 입력 영상. 그레이스케일 영상.
- maxValue: 임계값 함수 최댓값. 보통 255.
- adaptiveMethod: 블록 평균 계산 방법 지정. cv2.ADAPTIVE_THRESH_MEAN_C는 산술 평균, cv2.ADAPTIVE_THRESH_GAUSSIAN_C는 가우시안 가중치 평균
- thresholdType: cv2.THRESH_BINARY 또는 cv2.THRESH_BINARY_INV 지정
- blockSize: 블록 크기. 3 이상의 홀수.
- C: 블록 내 평균값 또는 블록 내 가중 평균값에서 뺄 값. (x, y) 픽셀의 임계값으로 𝑇 (𝑥, 𝑦) = 𝜇𝐵 (𝑥, 𝑦) − 𝐶 를 사용
'''

import sys
import numpy as np
import cv2


# 입력 영상 불러오기
src = cv2.imread('img/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


# 지역 이진화 방법
def local_th():
    # 전역 이진화 by Otsu's method
    _, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # 지역 이진화 by Otsu's method
    dst2 = np.zeros(src.shape, np.uint8)

    bw = src.shape[1] // 4
    bh = src.shape[0] // 4

    # (4, 4) Size로 지역 분할
    for y in range(4):
        for x in range(4):
            src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
            dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
            cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)  # dst_를 출력으로 지정한다.

    # 결과 출력
    cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()
    cv2.destroyAllWindows()


# OpenCV 적응형이진화
def adaptive_th():  # local_th보다 시간이 오래 걸린다는 단점이 있다.
    def on_trackbar(pos):
        bsize = pos
        if bsize % 2 == 0:
            bsize = bsize - 1
        if bsize < 3:
            bsize = 3

        dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, bsize, 5)

        cv2.imshow('dst', dst)


    cv2.imshow('src', src)
    cv2.namedWindow('dst')
    cv2.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
    cv2.setTrackbarPos('Block Size', 'dst', 11)

    cv2.waitKey()
    cv2.destroyAllWindows()


local_th()
adaptive_th()
