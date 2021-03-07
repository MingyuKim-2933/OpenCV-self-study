'''
05 허프 변환: 원 검출

허프 변환을 응용하여 원을 검출할 수 있음
- 원의 방정식 -> 3차원 축적 평면?

속도 향상을 위해 Hough gradient method 사용
- 입력 영상과 동일한 2차원 평면 공간에서 축적 영상을 생성
- 에지 픽셀에서 그래디언트 계산
- 에지 방향에 따라 직선을 그리면서 값을 누적
- 원의 중심을 먼저 찾고, 적절한 반지름을 검출

단점
- 여러 개의 동심원을 검출 못함 -> 가장 작은 원 하나만 검출됨

 허프 변환 원 검출 함수

cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None) -> circles
- image: 입력 영상. (에지 영상이 아닌 일반 영상)
- method: OpenCV 4.2 이하에서는 cv2.HOUGH_GRADIENT만 지정 가능
- dp: 입력 영상과 축적 배열의 크기 비율. 1이면 동일 크기. 2이면 축적 배열의 가로, 세로 크기가 입력 영상의 반.
- minDist: 검출된 원 중심점들의 최소 거리
- circles: (cx, cy, r) 정보를 담은 numpy.ndarray. shape=(1, N, 3), dtype=np.float32.
- param1: Canny 에지 검출기의 높은 임계값
- param2: 축적 배열에서 원 검출을 위한 임계값
- minRadius, maxRadius: 검출할 원의 최소, 최대 반지름

허프 원 검출과 cv2.HOUGH_GRADIENT_ALT 방법
- OpenCV 4.3 버전부터 지원
- cv2.HOUGH_GRADIENT 방법보다 정확한 원 검출 가능
- 사용법: OpenCV 4.3.0 HoughCircles() 함수 설명 참고
'''

import sys
import numpy as np
import cv2

# 입력 이미지 불러오기
src = cv2.imread('img/dial.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(gray, (0, 0), 1.0)  # 원을 검출할 때는 blur 과정을 거치면 검출이 더 잘된다.


def on_trackbar(pos):
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')

    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=th, minRadius=rmin, maxRadius=rmax)

    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            radius = round(radius)  # radius 값으로 정수가 필요해 반올림해준다.
            cv2.circle(dst, (cx, cy), radius, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)


# 트랙바 생성
cv2.imshow('img', src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.waitKey()

cv2.destroyAllWindows()
