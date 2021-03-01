'''
04 영상의 회전
회전 변환(rotation transformation)
- 영상을 특정 각도만큼 회전시키는 변환 (반시계 방향)
- x' = cosθ·x + sinθ·y, y' = -sinθ·x + cosθ·y

영상의 회전 변환 행렬 구하기
cv2.getRotationMatrix2D(center, angle, scale) -> retval
- center: 회전 중심 좌표. (x, y) 튜플.
- angle: (반시계 방향) 회전 각도(degree). 음수는 시계 방향.
- scale: 추가적인 확대 비율
- retval: 2x3 어파인 변환 행렬. 실수형.

영상의 중앙 기준 회전 예제 동작
- 회전 중심 좌표를 원점으로 이동 -> 회전 변환 -> 회전 중심 좌표를 원래 위치로 이동 -> 출력
'''

import sys
import math
import numpy as np
import cv2


def rotation1():  # 원점을 기준으로 회전시킨다.
    src = cv2.imread('img/tekapo.bmp')

    if src is None:
        print('Image load failed!')
        sys.exit()

    rad = 20 * math.pi / 180
    aff = np.array([[math.cos(rad), math.sin(rad), 0],
                    [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

    dst = cv2.warpAffine(src, aff, (0, 0))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

    cv2.destroyAllWindows()


def rotation2():  # 영상의 가운데를 기준으로 회전시킨다.
    src = cv2.imread('img/tekapo.bmp')

    if src is None:
        print('Image load failed!')
        sys.exit()

    cp = (src.shape[1] / 2, src.shape[0] / 2)  # 영상의 가운데 점
    rot = cv2.getRotationMatrix2D(cp, 20, 0.5)  # scale을 0.5를 줘서 영상이 잘려나가지 않게 한다.

    dst = cv2.warpAffine(src, rot, (0, 0))

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

    cv2.destroyAllWindows()


rotation1()
rotation2()
