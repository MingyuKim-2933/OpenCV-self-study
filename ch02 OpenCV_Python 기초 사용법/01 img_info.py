'''
01 영상의 속성과 픽셀 값 처리
OpenCV는 영상 데이터를 numpy.ndarray로 표현

ndim: 차원 수. 2 = grayscale, 3 = color, 4 = alpha 값이 포함된 color
shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다.
size: 전체 원소 개수
dtype: 원소의 데이터 타입. 영상 데이터는 uint8(numpy에서 지원하는 데이터타입)

그레이 스케일 영상 : cv2.CV_8UC1 -> numpy.uint8, shape = (h, w)
컬러 영상 : cv2.CV_8UC3 -> numpy.uint8, shape = (h, w, 3)
'''

import cv2, sys
import numpy as np

img1 = cv2.imread('../googlelogo.png', cv2.IMREAD_GRAYSCALE)  # shape : (h, w)
img2 = cv2.imread('../googlelogo.png', cv2.IMREAD_COLOR)  # shape : (h, w, 3)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

print(type(img1))
print(img1.shape)  # (1280, 1280)
print(img2.shape)  # (1280, 1280, 3)
print(img1.dtype)  # uint8
print(img2.dtype)  # uint8

h, w = img1.shape
print('h x w = {} x {}'.format(w, h))

h, w = img2.shape[:2]  # 컬러 영상은 슬라이싱을 사용해 앞의 두 개 값만 받아서 값에 대입해야한다.
print('h x w = {} x {}'.format(w, h))

if img1.ndim == 2:
    print('img1 is a grayscale image')

if len(img1.shape) == 2:
    print('img1 is a grayscale image')

x = 20
y = 10
p1 = img1[y, x]
print(p1)

p2 = img2[y, x]
print(p2)  # [255 255 255] (B G R) 순서로 출력된다.

# python에서 for문을 사용하여 이미지 처리를 하게 되면 연산속도가 느려 좋지 않다.(numpy나 opencv 라이브러리 활용하여 변경하자.)
'''
for y in range(h):
    for x in range(w):
        img1[y, x] = 0  # 검정색
        img2[y, x] = (0, 255, 255)  # 노란색
'''

# 위와 동일한 이미지 처리을 위해 아래 방법을 사용하는 것이 낫다.
img1[:, :] = 0  # :만 단독 사용하면 전체를 의미한다. 10까지 변경하고 싶으면 :10을 사용하자.
img2[:, :] = (0, 255, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()