'''
02 그래디언트와 에지 검출

영상의 그래디언트(gradient)
- 함수 f(x, y)를 x축과 y 축으로 각각 편미분(partial derivative)하여 벡터 형태로
표현한 것

실제 영상에서 구한 그래디언트 크기와 방향
- 그래디언트 크기: 픽셀 값의 차이 정도, 변화량
- 그래디언트 방향: 픽셀 값이 가장 급격하게 증가하는 방향

2D 벡터의 크기 계산 함수
cv2.magnitude(x, y, magnitude=None) -> magnitude (보통 float 형으로 준다.)
- x: 2D 벡터의 x 좌표 행렬. 실수형.
- y: 2D 벡터의 y 좌표 행렬. x와 같은 크기. 실수형.
- magnitude: 2D 벡터의 크기 행렬. x와 같은 크기, 같은 타입.

2D 벡터의 방향 계산 함수
cv2.phase(x, y, angle=None, angleInDegrees=None) -> angle
- x: 2D 벡터의 x 좌표 행렬. 실수형.
- y: 2D 벡터의 y 좌표 행렬. x와 같은 크기. 실수형.
- angle: 2D 벡터의 크기 행렬. x와 같은 크기, 같은 타입. angle(I) = atan2(y(I), x(I)) (만약 x(I)=y(I)=0이면 angle은 0으로 설정됨.)
- angleInDegrees: True이면 각도 단위, False이면 래디언 단위.
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)  # x 방향과 y 방향 두 방향의 미분을 사용한다.
mag = np.clip(mag, 0, 255).astype(np.uint8)

edge = np.zeros(mag.shape[:2], np.uint8)
edge[mag > 120] = 255
# _, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', edge)
cv2.waitKey()

cv2.destroyAllWindows()
