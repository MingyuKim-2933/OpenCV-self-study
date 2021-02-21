'''
03 컬러 영상과 색 공간

OpenCV와 컬러 영상
- 컬러 영상은 3차원 numpy.ndarray로 표현. img.shape(h,w,3)
- OpenCV에서는 RGB순서가 아니라 BGR순서를 기본으로 사용

RGB 색 공간
- 빛의 삼원색인 빨간색(R), 녹색(G), 파란색(B)을 혼합하여 색상을 표현(가산 혼합)
- TV & 모니터, 카메라 센서 Bayer필터, 비트맵

(색상)채널 분리
cv2.split(m, mv=None) -> dst
- m: 다채널 영상(e.g.) (B, G, R)로 구성된 컬러 영상
- mv: 출력 영상
- dst: 출력 영상의 리스트

(색상)채널 결합
cv2.merge(mv, dst=None) -> dst  # GrayScale 영상 3개가 나온다.
- mv: 입력 영상 리스트 또는 튜플
- dst: 출력 영상

색 공간 변환
- 영상 처리에서는 특정한 목적을 위해 RGB 색 공간을 HSV, YCrCb, Grayscale 등의 다른 색 공간으로 변환하여 처리

색 공간 변환 함수
cv2.cvtColor(src, code, dst=None, dstCn=None) -> dst
- src: 입력 영상
- code: 색 변환 코드  # cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2YCrCb 등 (OpenCV 문서 페이지 참고)
- dstCn: 결과 영상의 채널 수. 0이면 자동 결정.
- dst: 출력 영상

RGB 색상을 그레이스케일로 변환
Y = 0.299R + 0.587G + 0.114B
- 장점 : 데이터 저장 용량 감소, 데이터 처리 속도 향상
- 단점 : 색상 정보 손실

HSV 색 공간
- Hue: 색상, 색의 종류
- Saturation: 채도, 색의 탁하고 선명한 정도
- Value: 명도, 빛의 밝기

HSV값 범위
cv2.CV_8U 영상의 경우
- 0<=H<=179
- 0<=S<=255
- 0<=V<=255

YCrCb 색 공간
- PAL, NTSC, SECAM 등의 컬러 비디오 표준에 사용되는 색 공간
- 영상의 밝기 정보와 색상 정보를 따로 분리하여 부호화(흑백 TV호환)
- Y: 밝기 정보(luma)
- Cr, Cb: 색차(chroma)

YCrCb값 범위
cv2.CV_8U 영상의 경우
- 0<=Y<=255
- 0<=Cr<=255
- 0<=Cb<=255
'''

import sys
import numpy as np
import cv2

# 컬러 영상 불러오기
src = cv2.imread('img/candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)  # BGR 영상을 hsv 영상으로 변환
planes = cv2.split(src)  # 컬러 영상을 3개의 GrayScale 영상으로 분할
planes_hsv = cv2.split(src_hsv)

cv2.imshow('src', src)
cv2.imshow('src_hsv', src_hsv)
cv2.imshow('planes[0]', planes[0])  # Blue
cv2.imshow('planes[1]', planes[1])  # Green
cv2.imshow('planes[2]', planes[2])  # Red
cv2.waitKey()

cv2.destroyAllWindows()