'''
10 연산 시간 측정 방법
컴퓨터 비전은 대용량 데이터를 다루고, 일련의 과정을 통해 최종 결과를 얻으므로 매 단계에서 연산 시간을 측정하여 관리할 필요가 있음.
연산 시간은 loop를 통하여 여러 번 측정 후 평균 시간으로 확인하는 것이 좋다.
cv2.tickMeter() -> tm
- tm: cv2.TickMeter 객체
- tm.start(): 시간 측정 시작
- tm.stop(): 시간 측정 끝
- tm.reset(): 시간 측정 초기화

- tm.getTimeSec(): 측정 시간을 초 단위로 반환
- tm.getTimeMilli(): 측정 시간을 밀리초 단위로 반환
- tm.getTimeMicro(): 측정 시간을 마이크로초 단위로 반환
'''

import sys
import numpy as np
import cv2
import time

img = cv2.imread('img/hongkong.jpg')

if img is None:
    print('image load failed!')
    sys.exit()

tm = cv2.TickMeter()
tm.start()
# t1 = time.time()  # time 라이브러리를 사용하는 방법도 가능하다.
edge = cv2.Canny(img, 50, 150)
# t2 = time.time()
# time = t2 - t1
print('Elapsed time: {}s.'.format(time))
tm.stop()
ms = tm.getTimeMilli()

print('Elapsed time: {}ms.'.format(ms))
