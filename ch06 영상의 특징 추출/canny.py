'''
03 캐니 에지 검출

좋은 에지 검출기의 조건 (J. Canny)
- 정확한 검출(Good detection): 에지가 아닌 점을 에지로 찾거나 또는 에지인데 에지로 찾지 못하는 확률을 최소화
- 정확한 위치(Good localization): 실제 에지의 중심을 검출
- 단일 에지(Single edge): 하나의 에지는 하나의 점으로 표현

캐니 에지 검출 단계
- 가우시안 필터링 -> 그래디언트 계산(크기&방향) -> 비최대 억제 -> 이중 임계값을 이용한 히스테리시스 에지 트래킹

캐니 에지 검출 1단계
- 가우시안 필터링 (Optional) 잡음 제거 목적

캐니 에지 검출 2단계
- 그래디언트 계산 (주로 소벨 마스크를 사용)

캐니 에지 검출 3단계
- 비최대 억제 (Non-maximum suppression)
- 하나의 에지가 여러 개의 픽셀로 표현되는 현상을 없애기 위하여 그래디언트 크기가 국지적 최대 (local maximum)인 픽셀만을 에지 픽셀로 설정
- 그래디언트 방향에 위치한 두 개의 픽셀을 조사하여 국지적 최대를 검사

캐니 에지 검출 4단계
- 히스테리시스 에지 트래킹 (Hysteresis edge tracking)
- 두 개의 임계값을 사용: TLow , THigh
- 강한 에지: 𝑓 ≥ 𝑇𝐻𝑖𝑔ℎ -> 최종 에지로 선정
- 약한 에지: 𝑇𝐿𝑜𝑤 ≤ 𝑓 < 𝑇𝐻𝑖𝑔ℎ
-> 강한 에지와 연결되어 있는 픽셀만 최종 에지로 선정

캐니 에지 검출 함수
cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None) -> edges
- image: 입력 영상
- threshold1: 하단 임계값
- threshold2: 상단 임계값
- edges: 에지 영상
- apertureSize: 소벨 연산을 위한 커널 크기. 기본값은 3.
- L2gradient: True이면 L2 norm 사용, False이면 L1 norm 사용. 기본값은 False. (True를 사용하면 더 정확한 값을 얻음.)

참고사항
- threshold1:threshold2 = 1:2 또는 1:3을 자주 쓰지만 영상에 따라 적당한 값으로 바뀔 수 있다.
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)  # threshold를 적절히 주는 것이 중요하다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
