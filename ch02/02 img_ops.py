'''
영상의 생성, 복사, 부분 영상 추출
numpy.empty(shape, dtype=float, ...) -> arr
numpy.zeros(shape, dtype=float, ...) -> arr
numpy.ones(shape, dtype=float, ...) -> arr
numpy.full(shape, fill_value, dtype=None, ...) -> arr

shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다.
dtype: 원소의 데이터 타입. 일반적인 영상이면 numpy.uint8지정
arr: 생성된 영상

-참고사항:
numpy.empty() 함수는 임의의 값으로 초기화된 배열을 생성
numpy.zeros() 함수는 0으로 초기화된 배열을 생성
numpy.ones() 함수는 1로 초기화된 배열을 생성
numpy.full() 함수는 fill_value로 초기화된 배열을 생성
'''
import numpy as np
import cv2

# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)
img2 = np.zeros((240, 320, 3), dtype=np.uint8)
img3 = np.ones((240, 320, 3), dtype=np.uint8)
img4 = np.full((240, 320), 128, dtype=np.uint8)

my_img1 = cv2.imread('../googlelogo.png')
my_img2 = my_img1  # img2에 img1 복사, img1이 바뀌면 img2도 바뀐다.
my_img3 = my_img1.copy()  # 완벽한 복사본을 만들어 img1이 바껴도 img3은 변화가 없다.

my_img2 = my_img1[500:1000, 1000:1500]  # 행(높이 : h)을 500~1000, 열(넓이 : w)을 1000~1500까지 자른 이미지를 생성한다.
my_img3 = my_img1[500:1000, 1000:1500].copy()

cv2.circle(my_img2, (50, 50), 20, (0, 0, 255), 40)  # ROI(Region of Interest, 관심영역) 형태를 지정해서 그 부분의 처리를 한다.

# my_img1[:, :] = (0, 255, 255)  # 컬러 이미지를 노란색으로 변경한다.

cv2.imshow('img1', my_img1)
cv2.imshow('img2', my_img2)
cv2.imshow('img3', my_img3)
# cv2.imshow('img4', my_img4)
cv2.waitKey()

cv2.destroyAllWindows()
