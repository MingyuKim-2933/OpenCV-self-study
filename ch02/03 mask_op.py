'''
03 마스크 연산과 ROI
ROI : Region of Interest, 관심 영역 -> 영상에서 특정 연산을 수행하고자 하는 임의의 부분 영역

마스크 연산 : OpenCV는 일부 함수에 대해 ROI 연산을 지원하며, 이 때 마스크 영상을 인자로 함께 전달해야 함
(e.g.) cv2.copyTo(), cv2.calcHist(), cv2.bitwise_or(), cv2.matchTemplate(), etc.
마스크 영상은 cv2.CV_8UC1 타입(그레이스케일 영상)
마스크 영상의 픽셀 값이 0이 아닌 위치에서만 연산이 수행됨
-> 보통 마스크 영상으로는 0 또는 255로 구성된 이진 영상(binary image)을 사용
'''

'''
cv2.copyTo(src, mask, dst=None) -> dst
- src: 입력 영상
- mask: 마스크 영상. cv2.CV_8U.(numpy.uint8) 0이 아닌 픽셀에 대해서만 복사 연산을 수행.
- dst: 출력 영상. 만약 src와 크기 및 타입이 같은 dst를 입력으로 지정하면 dst를 새로 생성하지 않고 연산을 수행 is None:
       그렇지 않으면 dst를 새로 생성하여 연산을 수행한 후 반환함.
'''

import sys
import cv2

# 마스크 영상을 이용한 영상 합성
src = cv2.imread('img/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('img/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)  # 마스크는 무조건 GRAYSCALE이여야 함
dst = cv2.imread('img/field.bmp', cv2.IMREAD_COLOR)
dst2 = cv2.imread('img/field.bmp', cv2.IMREAD_COLOR)

cv2.copyTo(src, mask, dst)  # src, mask, dst는 모두 사이즈가 같아야 함, src와 dst는 타입이 같아야 함.

# dst[mask > 0] = src[mask > 0]  # copyTo()의 결과와 같다.

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)

# --------------------------------------------

src2 = cv2.imread('img/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)  # 알파채널이 포함된 사진은 cv2.IMREAD_UNCHANGED를 사용해야 한다.
mask2 = src2[:, :, -1]  # 슬라이싱 부분을 잘 모르겠음.. 스터디 때 질문하기
src2 = src2[:, :, 0:3]
h, w = src2.shape[:2]
crop = dst[0:h, 0:w]  # crop을 변경하면서 dst도 함께 변경된다. ( .copy()를 안썼기 때문에)
cv2.copyTo(src2, mask2, crop)

cv2.imshow('src', src2)
cv2.imshow('crop', dst)
cv2.imshow('mask', mask2)
cv2.waitKey()

cv2.destroyAllWindows()
