'''
05 카메라와 동영상 처리하기 1
cv2.VideoCapture 클래스 : OpenCV에서는 카메라와 동영상으로부터 프레임(frame)을 받아오는 작업을 cv2.VideoCapture 클래스 하나로 처리함
open()으로 카메라 또는 동영상 파일을 열고 read()를 통해 프레임을 받아온다.
'''
import sys, cv2
'''
카메라 열기
cv2.VideoCapture(index, apiPreference=None) -> retval
- index: camera_id + domain_offset_id, 시스템 기본 카메라를 기본 방법으로 열려면 index에 0을 전달
- apiPreference: 선호하는 카메라 처리 방법을 지정
- retval: cv2.VideoCapture 객체

cv2.VideoCapture.open(index, apiPreference=None) -> retval
- retval: 성공하면 True, 실패하면 False.
'''

# # 카메라 처리하기
# cap = cv2.VideoCapture(0)  # 아래 두줄의 코드와 같은 역할을 한다.
# # cap = cv2.VideoCapture()
# # cap.open(0)
#
# if not cap.isOpened():
#     print('camera open failed!')
#     sys.exit()
#
# # cv2.VideoCapture.get(propID) -> retval
# # propId: 속성 상수. (e.g.) 프레임 가로, 세로 크기, 초당 프레임 수, 현재 프레임 번호 등등(OpenCV 공식 문서 참조)
# # retval: 성공하면 해당 속성 값, 실패하면 0.
#
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(w, h)
#
# # cv2.VideoCapture.set(propID, value) -> retval
# # propId: 속성 상수.
# # value: 속성 값
# # retval: 성공하면 해당 속성 값, 실패하면 False.
#
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
#
#
#
# while True:
#     ret, frame = cap.read()  # ret는 True 또는 False
#     edge = cv2.Canny(frame, 50, 150)  # edge 검출
#
#     if not ret:
#         break
#
#     cv2.imshow('frame', frame)
#     cv2.imshow('edge', edge)
#     if cv2.waitKey(20) == 27:  # ESC
#         break
# cap.release()
# cv2.destroyAllWindows()

# ------------------------------------------------------------------
# 동영상 처리하기
cap = cv2.VideoCapture('img/video1.mp4')  # 아래 두줄의 코드와 같은 역할을 한다.
# cap = cv2.VideoCapture()
# cap.open(0)

if not cap.isOpened():
    print('video open failed!')
    sys.exit()

# cv2.VideoCapture.get(propID) -> retval
# propId: 속성 상수. (e.g.) 프레임 가로, 세로 크기, 초당 프레임 수, 현재 프레임 번호 등등(OpenCV 공식 문서 참조)
# retval: 성공하면 해당 속성 값, 실패하면 0.

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)



while True:
    ret, frame = cap.read()  # ret는 True 또는 False
    edge = cv2.Canny(frame, 50, 150)  # edge 검출

    if not ret:  # 동영상의 경우 동영상이 종료되면 자동으로 ret이 False가 되어 while문을 빠져나간다.
        break

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    if cv2.waitKey(20) == 27:  # ESC
        break
cap.release()
cv2.destroyAllWindows()