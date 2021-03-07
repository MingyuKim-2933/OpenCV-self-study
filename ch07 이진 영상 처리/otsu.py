'''
02 자동 이진화: Otsu 방법

 Otsu 이진화 방법
- 입력 영상이 배경(background)과 객체(object) 두 개로 구성되어 있다고 가정 -> Bimodal histogram (두 개의 산이 솟아있는 모양)
- 임의의 임계값 T 에 의해 나눠지는 두 픽셀 분포 그룹의 분산이 최소가 되는 T 를 선택
- 일종의 최적화 알고리즘(optimization algorithm)
- Within-class variance 최소화 -> Between-class variance 최대화
- Recursion을 이용한 효율적 계산 → Fast
'''

import sys
import numpy as np
import cv2


src = cv2.imread('img/rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Otsu 이진화 방법을 사용하여 threshold를 th에 저장한다.
print("otsu's threshold:", th)  # 131

cv2.imshow('src', src)
cv2.imshow('dst', dst)  # 조명에 따라 이진화가 부분적으로 잘 안될 수 있다.
cv2.waitKey()
cv2.destroyAllWindows()
