'''
08 마우스 이벤트 처리하기
마우스 이벤트 콜백함수 등록 함수
cv2.setMouseCallback(windowName, onMouse, param=None) -> None
- windowName: 마우스 이벤트 처리를 수행할 창 이름
- onMouse: 마우스 이벤트 처리를 위한 콜백 함수 이름. 마우스 이벤트 콜백함수는 다음 형식을 따라야 함.
           onMouse(event, x, y, flags, param) -> None
           param: 콜백 함수에 전달할 데이터
onMouse(event, x, y, flags, param) -> None
- event: 마우스 이벤트 종류. cv2.EVENT_로 시작하는 상수.
- x, y: 마우스 이벤트 발생 좌표
- flags: 마우스 이벤트 발생 시 상태. cv2.EVENT_FLAG_로 시작하는 상수
- param: cv2.setMouseCallback() 함수에서 설정한 데이터.
'''

import sys
import numpy as np
import cv2

oldx = oldy = -1
def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: {}, {}'.format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVEMT_LBUTTONUP: {}, {}'.format(x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:  # flags를 사용할 땐 &를 써야 다른 키가 눌려져 있더라도 LBUTTON을 인식하여 동작한다.
            print('EVEMT_MOUSEMOVE: {}, {}'.format(x, y))
            # cv2.circle(img, (x, y), 5, (0, 0, 255), -1)  # 마우스를 클릭할 때 빨간 원이 그려진다. 빨리 움직이면 직선이 끊긴다.
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 5, cv2.LINE_AA)  # 마우스를 빨리 움직여도 부드러운 선이 그려진다.
            cv2.imshow('image', img)
            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.setMouseCallback('image', on_mouse)
cv2.waitKey()

cv2.destroyAllWindows()