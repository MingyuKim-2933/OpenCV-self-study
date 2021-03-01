'''
03 이미지 피라미드

이미지 피라미드(Image pyramid)란?
- 하나의 영상에 대해 다양한 해상도의 영상 세트를 구성한 것
- 보통 가우시안 블러링 & 다운샘플링 형태로 축소하여 구성

영상 피라미드 다운샘플링
cv2.pyrDown(src, dst=None, dstsize=None, borderType=None) -> dst
- src: 입력 영상
- dst: 출력 영상
- dstsize: 출력 영상 크기. 따로 지정하지 않으면 입력 영상의 가로, 세로 크기의 1/2로 설정.
- borderType 가장자리 픽셀 확장 방식

참고 사항
- 먼저 5x5 크기의 가우시안 필터를 적용
- 이후 짝수 행과 열을 제거하여(홀수 행과 열만 남김) 작은 크기의 영상을 생성

영상 피라미드 업샘플링
cv2.pyrUp(src, dst=None, dstsize=None, borderType=None) -> dst
- src: 입력 영상
- dst: 출력 영상
- dstsize: 출력 영상 크기.
따로 지정하지 않으면 입력 영상의 가로, 세로 크기의 2배 설정.
- borderType 가장자리 픽셀 확장 방식
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple

# 원본 영상에 사각형 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 사각형 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')  # 잔상을 남기지 않는다.

cv2.destroyAllWindows()
