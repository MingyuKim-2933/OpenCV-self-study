'''
01 영상의 밝기 조절

영상의 화소 처리 기법
화소 처리
- 입력 영상의 특정 좌표 픽셀 값을 변경하여 출력 영상의 해당 좌표 픽셀 값으로 설정하는 연산
  dst(x, y) = f(src(x, y))  # f는 변환 함수(transfer function)이다.

- 결과 영상의 픽셀 값이 정해진 범위(e.g. 그레이스케일)에 있어야 함
- 반전, 밝기 조절, 명암비 조절 등등

밝기 조절이란?
- 영상을 전체적으로 더욱 밝거나 어둡게 만드는 연산
- 밝기 조절 수식 : dst(x, y) = saturate(src(x, y) + n)
  saturate 연산 : 영상의 픽셀 값이 255를 넘어가면 255로 제한하고 0 밑으로 내려가면 0으로 제한해주는 연산

영상의 밝기 조절을 위한 영상의 덧셈 연산
cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst
- src1: (입력)첫 번째 영상 또는 스칼라
- src2: (입력)두 번째 영상 또는 스칼라
- dst: (출력)덧셈 연산의 결과 영상
- mask: 마스크 영상
- dtype: 출력 영상(dst)의 타입. (e.g.) cv2.CV_8U, cv2.CV_32F 등

참고 사항
- 스칼라는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플
- dst를 함수 인자로 전달하려면 dst의 크기가 src1, src2와 같아야 하며, 타입이 적절해야함
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/lenna.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2. add(src, 100)
# dst = src + 100  # Uint8형식이라 255보다 값이 커지면 어두워진다.
# dst = np.clip(src + 100., 0, 255).astype(np.uint8)  # .을 붙여 실수타입으로 변경시킨 후 astype을 사용하여 uint8로 변경해야 add()와 같은 값을 얻을 수 있다.

src2 = cv2.imread('img/lenna.bmp')

dst2 = cv2. add(src2, (100, 100, 100, 0))  # 컬러 영상으로 받을 때는 실수 값 네 개로 구성된 튜플을 사용하여 BGR의 값을 각각 받아야 한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('src2', src2)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
