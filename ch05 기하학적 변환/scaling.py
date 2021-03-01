'''
02 영상의 확대와 축소
크기 변환(Scale transformation)
- 영상의 크기를 원본 영상보다 크게 또는 작게 만드는 변환
- x축과 y축 방향으로의 스케일 비율(scale factor)를 지정

cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None) -> dst
- src: 입력 영상
- dsize: 결과 영상 크기. (w, h) 튜플. (0, 0)이면 fx와 fy 값을 이용하여 결정.
- dst: 출력 영상
- fx, fy: x와 y방향 스케일 비율(scale factor). (dsize 값이 0일 때 유효)
- interpolation: 보간법 지정. 기본값은 cv2.INTER_LINEAR

interpolation parameter
- cv2.INTER_NEAREST 최근방 이웃 보간법
- cv2.INTER_LINEAR 양선형 보간법 (2x2 이웃 픽셀 참조)
- cv2.INTER_CUBIC 3차회선 보간법 (4x4 이웃 픽셀 참조)
- cv2.INTER_LANCZOS4 Lanczos 보간법 (8x8 이웃 픽셀 참조)
- cv2.INTER_AREA 영상 축소 시 효과적

영상의 축소 시 고려할 사항
- 영상 축소 시 디테일이 사라지는 경우가 발생 (e.g. 한 픽셀로 구성된 선분)
- 입력 영상을 부드럽게(blur처리) 필터링한 후 축소, 다단계 축소
- OpenCV의 cv2.resize() 함수에서는 cv2.INTER_AREA 플래그를 사용(축소에 적합함)

영상의 대칭 변환 (영상을 대칭(크기)변환 한 후 shift해서 구현된다.)
cv2.flip(src, flipCode, dst=None) -> dst
- src: 입력 영상
- flipCode: 대칭 방향 지정 (양수(+1): 좌우 대칭, 0: 상하 대칭, 음수(-1) 좌우 & 상하 대칭)
- dst: 출력 영상
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

# 내려갈수록 품질이 좋아지고 연산속도는 늘어난다.
dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800])
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()
