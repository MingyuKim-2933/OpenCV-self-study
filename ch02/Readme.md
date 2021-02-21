# ch02 OpenCV-Python 기초 사용법

## [01 img_info.py : 영상의 속성과 픽셀 값 처리](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02/01%20img_info.py)
01 영상의 속성과 픽셀 값 처리<br>
OpenCV는 영상 데이터를 numpy.ndarray로 표현 <br>
ndim: 차원 수. 2 = grayscale, 3 = color, 4 = alpha 값이 포함된 color <br>
shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다. <br>
size: 전체 원소 개수<br>
dtype: 원소의 데이터 타입. 영상 데이터는 uint8(numpy에서 지원하는 데이터타입) <br>
그레이 스케일 영상 : cv2.CV_8UC1 -> numpy.uint8, shape = (h, w) <br>
컬러 영상 : cv2.CV_8UC3 -> numpy.uint8, shape = (h, w, 3) <br>

## 02 img_ops.py : 영상의 생성, 복사, 부분 영상 추출

## 03 mask_op.py : 마스크 연산과 ROI

## 04 drawing.py : OpenCV 그리기 함수

## 05 camera_in.py : 카메라와 동영상 처리하기1

## 06 video_out.py : 카메라와 동영상 처리하기 2

## 07 keyboard.py : 키보드 이벤트 처리하기

## 08 mouse.py : 마우스 이벤트 처리하기

## 09 Trackbar.py : 트랙바 사용하기

## 10 time_check.py : 연산 시간 측정 방법
