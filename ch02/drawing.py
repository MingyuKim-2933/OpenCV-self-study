'''
OpenCV 그리기 함수
- OpenCV는 영상에 선, 도형, 문자열을 출력하는 그리기 함수를 제공
- 선 그리기 : 직선, 화살표, 마커 등
- 도형 그리기 : 사각형, 원, 타원, 다각형 등
- 문자열 출력

그리기 함수 사용 시 주의할 점
- 그리기 알고리즘을 이용하여 영상의 픽셀 값 자체를 변경 -> 원본 영상이 필요하면 복사본을 만들어서 그리기 & 출력
- 그레이스케일 영상에는 컬러로 그리기 안 됨 -> cv2.cvtColor() 함수로 BGR 컬러 영상으로 변환한 후 그리기 함수 호출
'''

import numpy as np
import cv2

'''
직선 그리기
cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> img
- img: 그림을 그릴 영상
- pt1, pt2: 직선의 시작점과 끝점
- color: 선 색상 또는 밝기. (B,G,R)튜플 또는 정수값.
- thickness: 선 두께. default는 1.
- lineType: 선 타입. cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA(안티앨리어싱 : 부드러운 선)중 선택. default는 cv2.LINE_8
- shift: 그리기 좌표 값의 축소 비율. default는 0.
'''

img = np.full((400, 400, 3), 255, np.uint8)

cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)  # (50,50)에서 (200, 50)으로 연결되는 빨간색 굵기 5의 직선
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))  # (50,50)에서 (200, 50)으로 연결되는 빨간색 굵기 5의 직선

'''
사각형 그리기
cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None) -> img
cv2.rectangle(img, rec, color, thickness=None, lineType=None, shift=None) -> img
- img: 그림을 그릴 영상
- pt1, pt2: 사각형의 두 꼭지점 좌표. (x1, y1) 튜플.
- rec: 사각형 위치 정보. (x, y, w, h) 튜플.
- color: 선 색상 또는 밝기. (B,G,R)튜플 또는 정수값.
- thickness: 선 두께. default는 1. 음수(-1)를 지정하면 내부를 채움.
- lineType: 선 타입. cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA(안티앨리어싱 : 부드러운 선)중 선택. default는 cv2.LINE_8
- shift: 그리기 좌표 값의 축소 비율. default는 0.
'''
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)  # (50, 200) 에서 시작해서 가로로 150 높이로 100이 되는 사각형을 그린다.
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)  # (70, 220)에서 (180, 220)을 대각선 양 끝점으로 하여 사각형을 그린다.

'''
원 그리기
cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None) -> img
- img: 그림을 그릴 영상
- center: 원의 중심 좌표. (x, y) 튜플.
- radius: 원의 반지름
- color: 선 색상 또는 밝기. (B,G,R)튜플 또는 정수값.
- thickness: 선 두께. default는 1. 음수(-1)를 지정하면 내부를 채움.
- lineType: 선 타입. cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA(안티앨리어싱 : 부드러운 선)중 선택. default는 cv2.LINE_8
- shift: 그리기 좌표 값의 축소 비율. default는 0.
'''

cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)  # 원, 타원, 문자열같이 곡선이 많을 때 cv2.LINE_AA를 사용해 부드럽게 만들어주면 좋다.
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

'''
다각형 그리기
cv2.polylines(img, pts, isClosed, color, thickness=None, lineType=None, shift=None) -> img
- img: 그림을 그릴 영상
- pts: 다각형 외곽 점들의 좌표 배열. numpy.ndarray의 리스트. (e.g.) [np.array([[10, 10], [50, 50], [10, 50]], dtype=np.int32)]
- isClosed: 폐곡선 여부. True 또는 False 지정
- color: 선 색상 또는 밝기. (B,G,R)튜플 또는 정수값.
- thickness: 선 두께. default는 1. 음수(-1)를 지정하면 내부를 채움.
- lineType: 선 타입. cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA(안티앨리어싱 : 부드러운 선)중 선택. default는 cv2.LINE_8
- shift: 그리기 좌표 값의 축소 비율. default는 0.
'''

pts = np.array([[250, 200], [300, 200], [350, 300], [250,300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)

'''
문자열 출력
cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None) -> img
- img: 그림을 그릴 영상
- text: 출력할 문자열
- org: 영상에서 문자열을 출력할 위치의 좌측 하단 좌표
- fontFace: 폰트 종류. cv2.FONT_HERSHEY_로 시작하는 상수 중 선택
- fontScale: 폰트 크기 확대/축소 비율
- color: 선 색상 또는 밝기. (B,G,R)튜플 또는 정수값.
- thickness: 선 두께. default는 1. 음수(-1)를 지정하면 내부를 채움.
- lineType: 선 타입. cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA(안티앨리어싱 : 부드러운 선)중 선택. default는 cv2.LINE_8
- bottomLeftOrigin: True이면 영사의 좌측 하단을 원점으로 간주.
'''

text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

# ----------------------- 출력

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()