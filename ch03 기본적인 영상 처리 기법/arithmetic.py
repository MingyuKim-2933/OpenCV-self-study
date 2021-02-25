'''
02 영상의 산술 연산

1) 덧셈 연산
dst(x, y) = saturate(src1(x, y) + src2(x,y)) # saturate 연산 : 영상의 픽셀 값이 255를 넘어가면 255로 제한하고 0 밑으로 내려가면 0으로 제한해주는 연산
- 두 영상의 같은 위치에 존재하는 픽셀 값을 더하여 결과 영상의 픽셀 값으로 설정한다.
- 덧셈 결과가 255보다 크면 픽셀 값을 255로 설정 (포화 연산)

cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst
- src1: (입력)첫 번째 영상 또는 스칼라
- src2: (입력)두 번째 영상 또는 스칼라
- dst: (출력)덧셈 연산의 결과 영상
- mask: 마스크 영상
- dtype: 출력 영상(dst)의 타입. (e.g.) cv2.CV_8U, cv2.CV_32F 등 (OpenCV 타입)

참고 사항
- 스칼라는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플
- dst를 함수 인자로 전달하려면 dst의 크기가 src1, src2와 같아야 하며, 타입이 적절해야함

2) 가중치 합(weighted sum)
dst(x, y) = saturate(α·src1(x, y) + β·src2(x,y))
- 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 가중 합을 계산하여 결과 영상의 픽셀 값으로 설정
- 보통 α + β = 1 이 되도록 설정-> 두 입력 영상의 평균 밝기를 유지

cv2.add(src1, alpha, src2, beta, gamma, dst=None, dtype=None) -> dst
- src1: 첫 번째 영상
- alpha: 첫 번째 영상 가중치
- src2: 두 번째 영상. src1과 같은 크기 & 같은 타입
- beta: 두 번째 영상 가중치
- gamma:  결과 영상에 추가적으로 더할 값
- dst: 가중치 합 결과 영상
- dtype: 출력 영상(dst)의 타입.

3) 평균 연산(average)
dst(x, y) = 1/2(src1(x, y) + src2(x,y))
- 가중치를 α = β = 0.5로 설정한 가중치 합

4) 뺄셈 연산
dst(x, y) = saturate(src1(x, y) - src2(x,y)) # saturate 연산 : 영상의 픽셀 값이 255를 넘어가면 255로 제한하고 0 밑으로 내려가면 0으로 제한해주는 연산
- 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 뺄셈 연산을 수행하여 결과 영상의 픽셀 값으로 설정한다.
- 덧셈 결과가 0보다 작으면 픽셀 값을 0으로 설정 (포화 연산)

cv2.subtract(src1, src2, dst=None, mask=None, dtype=None) -> dst
- src1: 첫 번째 영상 또는 스칼라
- src2: 두 번째 영상 또는 스칼라
- dst: 뺄셈 연산의 결과 영상
- mask: 마스크 영상
- dtype: 출력 영상(dst)의 타입. (e.g.) cv2.CV_8U, cv2.CV_32F 등 (OpenCV 타입)

5) 차이 연산
dst(x, y) = |src1(x, y) - src2(x, y)|
- 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 뺄셈 연산을 수행한 후, 그 절댓값을 결과 영상의 픽셀 값으로 설정
- 뺄셈 연산과 달리 입력 영상의 순서에 영향을 받지 않음

cv2.absdiff(src1, src2, dst=None) ->dst
- src1: 첫 번째 영상 또는 스칼라
- src2: 두 번째 영상 또는 스칼라
- dst: 차이 연산 결과 영상(차영상)

6) 영상의 논리 연산
비트단위 AND, OR, XOR, NOT 연산
cv2.bitwise_and(src1, src2, dst=None, mask=None) -> dst
cv2.bitwise_or(src1, src2, dst=None, mask=None) -> dst
cv2.bitwise_xor(src1, src2, dst=None, mask=None) -> dst
cv2.bitwise_not(src1, src2, dst=None, mask=None) -> dst

- src1: 첫 번째 영상 또는 스칼라
- src2: 두 번째 영상 또는 스칼라
- dst: 출력 영상
- mask: 마스크 영상

참고사항
-각각의 픽셀 값을 이진수로 표현하고, 비트(bit)단위 논리 연산을 수행
'''

import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

src1 = cv2.imread('img/lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('img/square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')  # 231은 2행3열중 첫번째
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()