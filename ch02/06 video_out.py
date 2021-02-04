'''
06 카메라와 동영상 처리하기 2
cv2.VideoWriter 클래스 : OpenCV에서는 cv2.VideoWriter 클래스를 이용하여 일련의 프레임을 동영상 파일로 저장할 수 있음
일련의 프레임은 모두 크기와 데이터 타입이 같아야 함

Fourcc(4-문자 코드, four character code) : 동영상 파일의 코덱, 압축 방식, 색상, 픽셀 포맷 등을 정의하는 정수 값
cv2.VideoWriter_fourcc(*'DIVX') - DIVX MPEG-4 코덱
cv2.VideoWriter_fourcc(*'XVID') - XVID MPEG-4 코덱
cv2.VideoWriter_fourcc(*'FMP4') - FFMPEG MPEG-4 코덱
cv2.VideoWriter_fourcc(*'X264') - H.264/AVC 코덱
cv2.VideoWriter_fourcc(*'MJPG') - Motion-JPEG 코덱
'''
import cv2, sys
'''
저장을 위한 동영상 파일 열기
cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=None) -> retval
- filename: 비디오 파일 이름 (e.g. 'video.mp4')
- fourcc: fourcc (e.g. cv2.VideoWriter_fourcc(*'DIVX'))
- fps: 초당 프레임 수 (e.g. 30)
- frameSize: 프레임 크기 (e.g. [640, 480])  # 튜플 형태
- isColor: 컬러 영상이면 True, 그렇지 않으면 False
- retval: cv2.VideoWriter 객체

cv2.VideoWriter.open(filename, fourcc, fps, frameSize, isColor=None) -> retval
- retval: 성공하면 True, 실패하면 False.
'''

# 웹 카메라 입력을 동영상으로 저장하기
cap = cv2.VideoCapture(0)

# round는 파이썬에서 지원하는 반올림 함수
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # *'DIVX == 'D', 'I', 'V', 'X'
fps = cap.get(cv2.CAP_PROP_FPS)
delay = round(1000 / fps)  # 한 프레임과 다음 프레임 사이의 시간 간격 (밀리세컨드 단위)
out = cv2.VideoWriter('output.avi', fourcc, 30, (w, h))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame  # ~frame은 색 반전 시켜준다.
    out.write(inversed)  # inversed 영상을 저장하여 동영상 파일로 만들어준다. 이 때 소리를 제외한 영상만 저장이 된다.

    edge = cv2.Canny(frame, 50, 150)
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    if cv2.waitKey(10) == 27:
        break