'''
09 크로마 키 합성

크로마 키(Chroma key) 합성이란?
- 녹색 또는 파란색 배경에서 촬영한 영상에 다른 배경 영상을 합성하는 기술

구현 할 기능
- 녹색 스크린 영역 추출하기
- 녹색 영역에 다른 배경 영상을 합성하여 저장하기
- 스페이스바를 이용하여 크로마 키 합성 동작 제어하기

녹색 스크린 영역 추출하기
- 크로마 키 영상을 HSV 색 공간으로 변환
- cv2.inRange()함수를 사용하여 50<=H<=80, 150 <=S<=255, 0<=V<=255 범위의 영역을 검출

녹색 영역에 다른 배경 영상을 합성하기
- 마스크 연산을 지원하는 cv2.copyTo()함수 사용
'''

import sys
import numpy as np
import cv2

# 녹색 배경 동영상
cap1 = cv2.VideoCapture('img/woman.mp4')

if not cap1.isOpened():
    print('cap1 open failed!')
    sys.exit()

# 비오는 배경 동영상
cap2 = cv2.VideoCapture('img/raining.mp4')

if not cap2.isOpened():
    print('cap2 open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print('w x h: {} x {}'.format(w, h))
print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

# 출력 동영상 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 합성 여부 플래그
do_composit = False

# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    # do_composit 플래그가 True일 때에만 합성
    if do_composit:
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (80, 255, 255))
        cv2.copyTo(frame2, mask, frame1)

    out.write(frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # 스페이스바를 누르면 do_composit 플래그를 변경
    if key == ord(' '):
        do_composit = not do_composit

    elif key == 27:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
