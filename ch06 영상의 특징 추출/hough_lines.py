'''
04 허프 변환: 직선 검출

허프 변환(Hough transform) 직선 검출이란?
- 2차원 영상 좌표에서의 직선의 방정식을 파라미터(parameter) 공간으로 변환하여 직선을 찾는 알고리즘
y = ax + b <-> b = -xa + y

축적 배열(accumulation array)
- 직선 성분과 관련된 원소 값을 1씩 증가시키는 배열

직선의 방정식 y = ax + b 를 사용할 때의 문제점
- y 축과 평행한 수직선을 표현하지 못함 -> 극좌표계 직선의 방정식을 사용
xcosθ + ysinθ = ρ (극 좌표계 직선의 방정식)

허프 변환에 의한 선분 검출
cv2.HoughLines(image , rho , theta , threshold , lines=None , srn=None , stn=None, min_theta=None , max_theta=None)-> lines
- image: 입력 에지 영상
- rho: 축적 배열에서 rho 값의 간격 . (e.g.) 1.0  1 픽셀 간격
- theta: 축적 배열에서 theta 값의 간격 . (e.g.) np.pi / 180  1  간격
- threshold: 축적 배열에서 직선으로 판단할 임계값
- lines: 직선 파라미터 (rho, theta) 정보를 담고 있는 numpy.ndarray. shape=(N, 1, 2). dtype numpy.float32
- srn , stn : 멀티 스케일 허프 변환에서 rho 해상도 , theta 해상도를 나누는 값 기본값은 0 이고 , 이 경우 일반 허프 변환 수행
- min_theta , max_theta : 검출할 선분의 최소 , 최대 theta 값

확률적 허프 변환에 의한 선분 검출
cv2.HoughLinesP(image, rho, theta, threshold, lines=None, minLineLength=None, maxLineGap=None) -> lines
- image: 입력 에지 영상
- rho: 축적 배열에서 rho 값의 간격. (e.g.) 1.0 → 1픽셀 간격.
- theta: 축적 배열에서 theta 값의 간격. (e.g.) np.pi / 180 → 1 간격.
- threshold: 축적 배열에서 직선으로 판단할 임계값
- lines: 선분의 시작과 끝 좌표(x1, y1, x2, y2) 정보를 담고 있는 numpy.ndarray. shape=(N, 1, 4). dtype=numpy.int32.
- minLineLength: 검출할 선분의 최소 길이
- maxLineGap: 직선으로 간주할 최대 에지 점 간격
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)  # edge 영상으로 변환

lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160, minLineLength=50, maxLineGap=5)  # 파라미터 값이 중요하다.

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:  # 찾은 line을 빨간색으로 시각화한다.
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
