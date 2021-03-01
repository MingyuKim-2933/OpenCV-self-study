'''
05 어파인 변환과 투시 변환

어파인 변환(Affine Transform)
- Translation
- Shear
- Scaling
- Rotation
- Parallelograms
- 2x3 matrix(6 DOF)
- 점 3개의 이동을 알아야 함

투시 변환(Perspective Transform)
- Trapazoids
- 3x3 matrix(8 DOF)
- 점 4개의 이동을 알아야 함

어파인 변환 행렬 구하기
cv2.getAffineTransform(src, dst) -> retval
- src: 3개의 원본 좌표점. numpy.ndarray. shape=(3, 2)  e.g) np.array([[x1, y1], [x2, y2], [x3, y3]], np.float32)
- dst: 3개의 결과 좌표점. numpy.ndarray. shape=(3, 2)
- retval: 2x3 투시 변환 행렬

투시 변환 행렬 구하기
cv2.getPerspectiveTransform(src, dst, solveMethod=None) -> retval
- src: 4개의 원본 좌표점. numpy.ndarray. shape=(4, 2)  e.g) np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], np.float32)
- dst: 4개의 결과 좌표점. numpy.ndarray. shape=(4, 2)
- retval: 3x3 투시 변환 행렬

영상의 어파인 변환 함수

cv2.warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None) -> dst
- src: 입력 영상
- M: 2x3 어파인 변환 행렬. 실수형.
- dsize: 결과 영상 크기. (w, h) 튜플. (0, 0)이면 src와 같은 크기로 설정.
- dst: 출력 영상
- flags: 보간법. 기본값은 cv2.INTER_LINEAR.
- borderMode: 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT.
- borderValue: cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본값은 0.
'''

import sys
import numpy as np
import cv2

src = cv2.imread('img/namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)  # 명함의 4개 점
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
