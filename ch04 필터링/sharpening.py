'''
04 샤프닝: 언샤프 마스크 필터

언샤프 마스크(Unsharp mask) 필터링
- 날카롭지 않은(unsharp) 영상, 즉, 부드러워진 영상(blur처리된 영상)을 이용하여 날카로운 영상을 생성

언샤프 마스크 필터 구현하기
- 샤프닝 정도를 조절할 수 있도록 수식 변경
h(x, y) = f(x, y) + α·g(x, y) -> h(x, y) = (1+α)f(x, y) - α·Gsigma(f(x, y))

OpenCV에서 제공되는 함수가 없어 직접 구현해야 한다.
'''

import sys
import numpy as np
import cv2


def sharpening1():  # 그레이스케일 영상에 언샤프 마스크 필터 적용하기
    src = cv2.imread('img/rose.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        sys.exit()

    blr = cv2.GaussianBlur(src, (0, 0), 2)
    dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)  # blr 영상을 활용하여 sharpening해준다.
    # dst = cv2.addWeighted(src, 2, blr, -1, 0)  # 위의 결과와 같다. (src를 2배한 영상에서 blr 영상을 뺀다.)
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

    cv2.destroyAllWindows()


def sharpening2():  # 컬러 영상에 언샤프 마스크 필터 적용하기
    src = cv2.imread('img/rose.bmp')

    if src is None:
        print('Image load failed!')
        sys.exit()

    src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

    src_f = src_ycrcb[:, :, 0].astype(np.float32)  # 계산을 정교하게 하기 위해 실수형으로 변경시킨다.
    blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
    src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)  # 최종적으로 영상을 uint8 형태로 출력한다.

    dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

    cv2.destroyAllWindows()


sharpening1()
sharpening2()