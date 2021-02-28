'''
06 잡음 제거(2): 양방향 필터

가우시안 필터
- 가우시안 잡음 제거에는 가우시안 필터가 효과적

양방향 필터(Bilateral filter)
- 에지 보전 잡음 제거 필터(edge-preserving noise removal filter)의 하나
- 평균 값 필터 또는 가우시안 필터는 에지 부근에서도 픽셀 값을 평탄하게 만드는
단점이 있음
- 기준 픽셀과 이웃 픽셀과의 거리, 그리고 픽셀 값의 차이를 함께 고려하여 블러링
정도를 조절

(일반적인) 가우시안 필터링: 영상 전체에서 blurring <-> 양방향 필터: 에지가 아닌 부분에서만 blurring

양방향 필터링 함수 (엣지 부분은 살아있고 평탄한 부분에서만 노이즈가 제거된다.)
cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None) -> dst
- src: 입력 영상. 8비트 또는 실수형, 1채널 또는 3채널.
- d: 필터링에 사용될 이웃 픽셀의 거리(지름). 음수(-1)를 입력하면 sigmaSpace 값에 의해 자동 결정됨. (자동 결정 되게 두는 것이 좋다.)
- sigmaColor: 색 공간에서 필터의 표준 편차
- sigmaSpace: 좌표 공간에서 필터의 표준 편차
- dst: 출력 영상. src와 같은 크기, 같은 타입.
- borderType: 가장자리 픽셀 처리 방식
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)  # d 값에 -1 주는 것이 좋다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

