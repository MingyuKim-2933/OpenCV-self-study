'''
03 블러링(2): 가우시안 필터

평균값 필터에 의한 블러링의 단점
- 필터링 대상 위치에서 가까이 있는 픽셀과 멀리 있는 픽셀이 모두 같은 가중치를
사용하여 평균을 계산
- 멀리 있는 픽셀의 영향을 많이 받을 수 있음

가우시안 함수
- 가까운 픽셀은 큰 가중치를, 멀리 있는 픽셀은 작은 가중치를 사용하여 평균 계산

가우시안 함수의 특징
- Symmetric (bell curve) shape around the mean
- mean = median = mode

가우시안 필터링 함수
cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None) -> dst
- src: 입력 영상. 각 채널 별로 처리됨.
- dst: 출력 영상. src와 같은 크기, 같은 타입.
- ksize: 가우시안 커널 크기. (0, 0)을 지정하면 sigma 값에 의해 자동 결정됨. (값을 (0,0)으로 지정해 자동 결정하는 것이 좋음)
- sigmaX: x방향 sigma.
- sigmaY: y방향 sigma. 0이면 sigmaX와 같게 설정.
- borderType: 가장자리 픽셀 확장 방식.
'''

import sys
import numpy as np
import cv2


def gaussian1():
    src = cv2.imread('img/rose.bmp', cv2.IMREAD_GRAYSCALE)

    dst = cv2.GaussianBlur(src, (0, 0), 3)  # sigma 값을 높이면 blur 효과가 강해진다. mean 필터보다 연산속도가 느리다.
    dst2 = cv2.blur(src, (7, 7))  # mean필터를 사용한 blur처리

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.imshow('dst2', dst2)
    cv2.waitKey()

    cv2.destroyAllWindows()


def gaussian2():
    src = cv2.imread('img/rose.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    cv2.imshow('src', src)

    for sigma in range(1, 6):  # sigma의 값을 1부터 5까지 차례대로 사용하여 블러 처리한다.
        # sigma 값을 이용하여 가우시안 필터링
        dst = cv2.GaussianBlur(src, (0, 0), sigma)

        desc = 'sigma = {}'.format(sigma)
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()  # 키를 입력할 때마다 다음 sigma 값으로 변경된다.

    cv2.destroyAllWindows()


gaussian1()
gaussian2()
