# ch02 OpenCV-Python 기초 사용법

## [01 img_info.py : 영상의 속성과 픽셀 값 처리](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/01%20img_info.py)
01 영상의 속성과 픽셀 값 처리

OpenCV는 영상 데이터를 numpy.ndarray로 표현  

ndim: 차원 수. 2 = grayscale, 3 = color, 4 = alpha 값이 포함된 color  
shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다.  
size: 전체 원소 개수  
dtype: 원소의 데이터 타입. 영상 데이터는 uint8(numpy에서 지원하는 데이터타입)  

그레이 스케일 영상 : cv2.CV_8UC1 -> numpy.uint8, shape = (h, w)  
컬러 영상 : cv2.CV_8UC3 -> numpy.uint8, shape = (h, w, 3)  

## [02 img_ops.py : 영상의 생성, 복사, 부분 영상 추출](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/02%20img_ops.py)
02 영상의 생성, 복사, 부분 영상 추출  

numpy.empty(shape, dtype=float, ...) -> arr  
numpy.zeros(shape, dtype=float, ...) -> arr  
numpy.ones(shape, dtype=float, ...) -> arr  
numpy.full(shape, fill_value, dtype=None, ...) -> arr  

- shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다.  
- dtype: 원소의 데이터 타입. 일반적인 영상이면 numpy.uint8지정  
- arr: 생성된 영상  

참고사항   
- numpy.empty() 함수는 임의의 값으로 초기화된 배열을 생성  
- numpy.zeros() 함수는 0으로 초기화된 배열을 생성  
- numpy.ones() 함수는 1로 초기화된 배열을 생성  
- numpy.full() 함수는 fill_value로 초기화된 배열을 생성  

## [03 mask_op.py : 마스크 연산과 ROI](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/03%20mask_op.py)
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

## [04 drawing.py : OpenCV 그리기 함수](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/04%20drawing.py)
04 OpenCV 그리기 함수  

- OpenCV는 영상에 선, 도형, 문자열을 출력하는 그리기 함수를 제공  
- 선 그리기 : 직선, 화살표, 마커 등  
- 도형 그리기 : 사각형, 원, 타원, 다각형 등  
- 문자열 출력  

그리기 함수 사용 시 주의할 점  
- 그리기 알고리즘을 이용하여 영상의 픽셀 값 자체를 변경 -> 원본 영상이 필요하면 복사본을 만들어서 그리기 & 출력  
- 그레이스케일 영상에는 컬러로 그리기 안 됨 -> cv2.cvtColor() 함수로 BGR 컬러 영상으로 변환한 후 그리기 함수 호출
  
## [05 camera_in.py : 카메라와 동영상 처리하기1](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/05%20camera_in.py)
05 카메라와 동영상 처리하기 1 

cv2.VideoCapture 클래스 : OpenCV에서는 카메라와 동영상으로부터 프레임(frame)을 받아오는 작업을 cv2.VideoCapture 클래스 하나로 처리함  
open()으로 카메라 또는 동영상 파일을 열고 read()를 통해 프레임을 받아온다.  

카메라 열기  
cv2.VideoCapture(index, apiPreference=None) -> retval  
- index: camera_id + domain_offset_id, 시스템 기본 카메라를 기본 방법으로 열려면 index에 0을 전달  
- apiPreference: 선호하는 카메라 처리 방법을 지정  
- retval: cv2.VideoCapture 객체  
cv2.VideoCapture.open(index, apiPreference=None) -> retval  
- retval: 성공하면 True, 실패하면 False.  

cv2.VideoCapture.get(propID) -> retval  
- propId: 속성 상수. (e.g.) 프레임 가로, 세로 크기, 초당 프레임 수, 현재 프레임 번호 등등(OpenCV 공식 문서 참조)  
- retval: 성공하면 해당 속성 값, 실패하면 0.  

cv2.VideoCapture.set(propID, value) -> retval
- propId: 속성 상수.
- value: 속성 값
- retval: 성공하면 해당 속성 값, 실패하면 False.

동영상 처리하기
- cv2.VideoCapture.get(propID) -> retval
- propId: 속성 상수. (e.g.) 프레임 가로, 세로 크기, 초당 프레임 수, 현재 프레임 번호 등등(OpenCV 공식 문서 참조)
- retval: 성공하면 해당 속성 값, 실패하면 0.

## [06 video_out.py : 카메라와 동영상 처리하기 2](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/06%20video_out.py)
06 카메라와 동영상 처리하기 2  

cv2.VideoWriter 클래스 : OpenCV에서는 cv2.VideoWriter 클래스를 이용하여 일련의 프레임을 동영상 파일로 저장할 수 있음  
일련의 프레임은 모두 크기와 데이터 타입이 같아야 함  
Fourcc(4-문자 코드, four character code) : 동영상 파일의 코덱, 압축 방식, 색상, 픽셀 포맷 등을 정의하는 정수 값  
cv2.VideoWriter_fourcc(*'DIVX') - DIVX MPEG-4 코덱  
cv2.VideoWriter_fourcc(*'XVID') - XVID MPEG-4 코덱  
cv2.VideoWriter_fourcc(*'FMP4') - FFMPEG MPEG-4 코덱  
cv2.VideoWriter_fourcc(*'X264') - H.264/AVC 코덱  
cv2.VideoWriter_fourcc(*'MJPG') - Motion-JPEG 코덱  

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

## [07 keyboard.py : 키보드 이벤트 처리하기](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/07%20keyboard.py)
07 키보드 이벤트 처리하기 

키보드 입력 대기 함수  
cv2.waitKey(delay=None) -> retval  
- delay: 밀리세컨드 단위 대기 시간. delay<=0이면 무한히 기다림. default는 0  
- retval: 눌린 키 값(ASCII code). 키가 눌리지 않으면 -1.  

참고 사항  
- cv2.waitKey() 함수는 OpenCV 창이 하나라도 있을 때 동작함  
- 특정 키 입력을 확인하려면 ord()함수를 이용  
    while True:  
        if cv2.waitKey() == ord('q'):  
            break  
- 주요 특수키 코드: 27(ESC), 13(ENTER), 9(TAB)  

키보드 특수키 입력 처리하기  
- Windows 운영체제에서 방향키, 함수키(Insert, Delete, F12) 등의 특수키 입력은 cv2.waitKeyEx() 함수 사용  

## [08 mouse.py : 마우스 이벤트 처리하기](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/08%20mouse.py)
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

## [09 Trackbar.py : 트랙바 사용하기](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/09%20Trackbar.py)
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

## [10 time_check.py : 연산 시간 측정 방법](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch02%20OpenCV_Python%20기초%20사용법/10%20time_check.py)
10 연산 시간 측정 방법  

컴퓨터 비전은 대용량 데이터를 다루고, 일련 과정을 통해 최종 결과를 얻으므로 매 단계에서 연산 시간을 측정하여 관리할 필요가 있음.  
연산 시간은 loop를 통하여 여러 번 측정 후 평균 시간으로 확인하는 것이 좋다.  
cv2.tickMeter() -> tm  
- tm: cv2.TickMeter 객체  
- tm.start(): 시간 측정 시작  
- tm.stop(): 시간 측정 끝  
- tm.reset(): 시간 측정 초기화  
- tm.getTimeSec(): 측정 시간을 초 단위로 반환  
- tm.getTimeMilli(): 측정 시간을 밀리초 단위로 반환  
- tm.getTimeMicro(): 측정 시간을 마이크로초 단위로 반환  
