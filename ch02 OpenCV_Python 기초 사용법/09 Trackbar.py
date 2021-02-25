'''
09 트랙바 사용하기
트랙바 : 프로그램 동작 중 사용자가 지정한 범위 안의 값을 선택할 수 있는 컨트롤
cv2.createTrackbar(trackbarName, windowName, value, count, onChange) -> None
- trackBarName: 트랙바 이름
- windowName: 트랙바를 생성할 창 이름
- value: 트랙바 위치 초기값
- count: 트랙바 최댓값. 최솟값은 항상 0
- onChange: 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름
            트랙바 이벤트 콜백 함수는 다음 형식을 따름.
            onChange(pos) -> None
'''

import numpy as np
import cv2


def on_level_changed(pos):
    global img

    level = pos * 16
    level = np.clip(level, 0, 255)  # np.clip()은 0보다 작을 땐 0으로 255보다 크면 255로 변경시켜 값을 제한해준다.

    img[:, :] = level  # 슬라이스 :만 넣었을 때는 모든 범위에 적용된다.
    cv2.imshow('image', img)


img = np.zeros((480, 640, 3), dtype=np.uint8)

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.createTrackbar('GrayLevel', 'image', 0, 16, on_level_changed)
cv2.waitKey()

cv2.destroyAllWindows()