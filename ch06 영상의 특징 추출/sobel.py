'''
01 영상의 미분과 소벨 필터

에지(edge)
- 영상에서 픽셀의 밝기 값이 급격하게 변하는 부분
- 일반적으로 배경과 객체, 또는 객체와 객체의 경계

기본적인 에지 검출 방법
- 영상을 (x, y) 변수의 함수로 간주했을 때, 이 함수의 1차 미분(1st derivative) 값이 크게 나타나는 부분을 검출

1차 미분의 근사화(approximation)
- 전진 차분 (Forward difference)
- 후진 차분 (Backward difference)
- 중앙 차분 (Centered difference) (가장 정확한 미분 방법으로 알려져있다.)

다양한 미분 마스크
- Prewitt
- Sobel (가장 많이 사용하는 마스크)
- Scharr

소벨 필터를 이용한 미분 함수
cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None) -> dst
- src: 입력 영상
- ddepth: 출력 영상 데이터 타입. -1이면 입력 영상과 같은 데이터 타입을 사용.
- dx: x 방향 미분 차수.
- dy: y 방향 미분 차수.
- dst: 출력 영상(행렬)
- ksize: 커널 크기. 기본값은 3.
- scale 연산 결과에 추가적으로 곱할 값. 기본값은 1.
- delta: 연산 결과에 추가적으로 더할 값. 기본값은 0.
- borderType: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_DEFAULT.

참고사항
- 대부분 dx=1, dy=0, ksize=3 또는 dx=0, dy=1, ksize=3으로 지정.

샤르 필터를 이용한 미분 함수 ( Sobel 필터에 비해 자주 사용되지 않음.)
cv2.Scharr(src, ddepth, dx, dy, dst=None, scale=None, delta=None, borderType=None) -> dst
- src: 입력 영상
- ddepth: 출력 영상 데이터 타입. -1이면 입력 영상과 같은 데이터 타입을 사용.
- dx: x 방향 미분 차수.
- dy: y 방향 미분 차수.
- dst: 출력 영상(행렬)
- scale 연산 결과에 추가적으로 곱할 값. 기본값은 1.
- delta: 연산 결과에 추가적으로 더할 값. 기본값은 0.
- borderType: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_DEFAULT.
'''

import sys
import numpy as np
import cv2


src = cv2.imread('img/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

''' 
# 직접 커널을 만들어서 edge를 검출하는 방법
kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]], dtype=np.float32)

dx = cv2.filter2D(src, -1, kernel, delta=128)
'''

# Sobel edge를 검출하는 cv2.Sobel()함수를 사용하여 edge를 검출하는 방법
dx = cv2.Sobel(src, -1, 1, 0, delta=128)  # x 방향의 변화를 가지고 영상을 미분한다.
dy = cv2.Sobel(src, -1, 0, 1, delta=128)  # y 방향의 변화를 가지고 영상을 미분한다.

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
