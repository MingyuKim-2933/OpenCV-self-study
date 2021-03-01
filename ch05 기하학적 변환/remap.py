'''
06 리매핑

리매핑(remapping)
- 영상의 특정 위치 픽셀을 다른 위치에 재배치하는 일반적인 프로세스
- dst(x, y) = src(map(x) (x, y),map(y) (x, y))
- 어파인 변환, 투시 변환을 포함한 다양한 변환을 리매핑으로 표현 가능

리매핑 함수
cv2.remap(src, map1, map2, interpolation, dst=None, borderMode=None, borderValue=None) -> dst
- src: 입력 영상
- map1: 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 x좌표. 입력 영상과 크기는 같고, 타입은 np.float32인 numpy.ndarray.
- map2: 결과 영상의 (x, y) 좌표가 참조할 입력 영상의 y좌표.
- interpolation: 보간법
- dst: 출력 영상
- borderMode: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT.
- borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.
'''

import sys
import numpy as np
import cv2


src = cv2.imread('img/tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

# np.indices(): 행렬의 x좌표값과 y좌표값을 따로 행렬의 형태로 반환한다.
map2, map1 = np.indices((h, w), dtype=np.float32)  # map2는 y좌표, map1은 x좌표
map2 = map2 + 10 * np.sin(map1 / 32)  # 출렁거리는 형태의 사진을 반환한다.

dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)  # BORDER_DEFAULT로 설정하면 검정색 픽셀 부분이 근처의 픽셀로 채워져서 자연스러워진다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
