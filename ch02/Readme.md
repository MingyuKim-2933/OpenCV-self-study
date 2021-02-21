# ch02 OpenCV-Python 기초 사용법

## [01 img_info.py : 영상의 속성과 픽셀 값 처리](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02/01%20img_info.py)
01 영상의 속성과 픽셀 값 처리  
OpenCV는 영상 데이터를 numpy.ndarray로 표현  

ndim: 차원 수. 2 = grayscale, 3 = color, 4 = alpha 값이 포함된 color  
shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다.  
size: 전체 원소 개수  
dtype: 원소의 데이터 타입. 영상 데이터는 uint8(numpy에서 지원하는 데이터타입)  

그레이 스케일 영상 : cv2.CV_8UC1 -> numpy.uint8, shape = (h, w)  
컬러 영상 : cv2.CV_8UC3 -> numpy.uint8, shape = (h, w, 3)  

## [02 img_ops.py : 영상의 생성, 복사, 부분 영상 추출](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02/02%20img_ops.py)
02 영상의 생성, 복사, 부분 영상 추출  
numpy.empty(shape, dtype=float, ...) -> arr  
numpy.zeros(shape, dtype=float, ...) -> arr  
numpy.ones(shape, dtype=float, ...) -> arr  
numpy.full(shape, fill_value, dtype=None, ...) -> arr  

shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다.  
dtype: 원소의 데이터 타입. 일반적인 영상이면 numpy.uint8지정  
arr: 생성된 영상  

-참고사항:  
numpy.empty() 함수는 임의의 값으로 초기화된 배열을 생성  
numpy.zeros() 함수는 0으로 초기화된 배열을 생성  
numpy.ones() 함수는 1로 초기화된 배열을 생성  
numpy.full() 함수는 fill_value로 초기화된 배열을 생성  

## [03 mask_op.py : 마스크 연산과 ROI](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02/03%20mask_op.py)
03 마스크 연산과 ROI  
ROI : Region of Interest, 관심 영역 -> 영상에서 특정 연산을 수행하고자 하는 임의의 부분 영역  

마스크 연산 : OpenCV는 일부 함수에 대해 ROI 연산을 지원하며, 이 때 마스크 영상을 인자로 함께 전달해야 함  
(e.g.) cv2.copyTo(), cv2.calcHist(), cv2.bitwise_or(), cv2.matchTemplate(), etc.  
마스크 영상은 cv2.CV_8UC1 타입(그레이스케일 영상)  
마스크 영상의 픽셀 값이 0이 아닌 위치에서만 연산이 수행됨  
-> 보통 마스크 영상으로는 0 또는 255로 구성된 이진 영상(binary image)을 사용  

cv2.copyTo(src, mask, dst=None) -> dst  
- src: 입력 영상  
- mask: 마스크 영상. cv2.CV_8U.(numpy.uint8) 0이 아닌 픽셀에 대해서만 복사 연산을 수행.  
- dst: 출력 영상. 만약 src와 크기 및 타입이 같은 dst를 입력으로 지정하면 dst를 새로 생성하지 않고 연산을 수행 is None:  
       그렇지 않으면 dst를 새로 생성하여 연산을 수행한 후 반환함.  

## [04 drawing.py : OpenCV 그리기 함수](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02/04%20drawing.py)
04 OpenCV 그리기 함수  
- OpenCV는 영상에 선, 도형, 문자열을 출력하는 그리기 함수를 제공  
- 선 그리기 : 직선, 화살표, 마커 등  
- 도형 그리기 : 사각형, 원, 타원, 다각형 등  
- 문자열 출력  
- 
그리기 함수 사용 시 주의할 점  
- 그리기 알고리즘을 이용하여 영상의 픽셀 값 자체를 변경 -> 원본 영상이 필요하면 복사본을 만들어서 그리기 & 출력  
- 그레이스케일 영상에는 컬러로 그리기 안 됨 -> cv2.cvtColor() 함수로 BGR 컬러 영상으로 변환한 후 그리기 함수 호출  
## [05 camera_in.py : 카메라와 동영상 처리하기1]()

## [06 video_out.py : 카메라와 동영상 처리하기 2]()

## [07 keyboard.py : 키보드 이벤트 처리하기]()

## [08 mouse.py : 마우스 이벤트 처리하기]()

## [09 Trackbar.py : 트랙바 사용하기]()

## [10 time_check.py : 연산 시간 측정 방법]()
