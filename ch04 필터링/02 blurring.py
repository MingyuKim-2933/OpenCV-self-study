'''
02 블러링(1): 평균 값 필터

평균 값 필터(Mean filter)
- 영상의 특정 좌표 값을 주변 픽셀 값들의 산술 평균으로 설정
- 픽셀들 간의 그레이스케일 값 변화가 줄어들어 날카로운 에지가 무뎌지고, 영상에 있는 잡음의 영향이 사라지는 효과
- 영상에 평균 값 필터를 적용할 때 마스크 크기가 커질수록 평균 값 필터 결과가 더욱 부드러워짐(블러 효과가 많이 적용됨) -> 더 많은 연산량 필요!
- 편한 블러링 방식이지만 퀄리티가 떨어지는 단점이 있다. (가우시안 필터가 퀄리티가 더 좋다.)

기본적인 2D 필터링
cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None) -> dst
- src: 입력 영상 (uint8 타입을 자주 사용)
- ddepth: 출력 영상 데이터 타입. (e.g) cv2.CV_8U, cv2.CV_32F, cv2.CV_64F (-1을 지정하면 src와 같은 타입의 dst 영상을 생성)
- kernel: 필터 마스크 행렬. 실수형.
- anchor: 고정점 위치. (-1, -1)이면 필터 중앙을 고정점으로 사용
- delta: 추가적으로 더할 값 (default 값은 0)
- borderType: 가장자리 픽셀 확장 방식
- dst: 출력 영상

평균 값 필터링 함수
cv2.blur(src, ksize, dst=None, anchor=None, borderType=None) -> dst
- src: 입력 영상
- ksize: 평균값 필터 크기. (width, height) 형태의 튜플.
- dst: 결과 영상. 입력 영상과 같은 크기 & 같은 타입.
- kernel = 1 / (ksize.width * ksize.height)
'''

import sys
import numpy as np
import cv2


def blurring1():
    src = cv2.imread('img/rose.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    kernel = np.array([[1/9, 1/9, 1/9],
                       [1/9, 1/9, 1/9],
                       [1/9, 1/9, 1/9]], dtype=np.float64)

    # kernel = np.ones((3, 3), dtype=np.float64) / 9  # 하나씩 입력하지 않고 이렇게 만들어주는 방법이 있다.

    dst = cv2.filter2D(src, -1, kernel)
    # dst = cv2.blur(src, (3, 3))  # cv2.blur()를 사용한 방법. 위의 결과와 동일하다.

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

    cv2.destroyAllWindows()


def blurring2():
    src = cv2.imread('img/rose.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    cv2.imshow('src', src)

    for ksize in (3, 5, 7):
        dst = cv2.blur(src, (ksize, ksize))

        desc = 'Mean: {}x{}'.format(ksize, ksize)  # 이미지 위에 텍스트를 적는다.
        cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)

        cv2.imshow('dst', dst)
        cv2.waitKey()

    cv2.destroyAllWindows()


blurring1()
blurring2()
