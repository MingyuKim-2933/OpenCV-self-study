# ch04 필터링

## [01 filtering.py : 필터링 이해하기](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch04%20%ED%95%84%ED%84%B0%EB%A7%81/filtering.py)
01 필터링 이해하기

영상의 필터링(image filtering)
- 영상에서 필요한 정보만 통과시키고 원치 않는 정보는 걸러내는 작업

주파수 공간에서의 필터링(Frequency domain filtering)  
- 저주파 성분 : 영상에서 부드러운 성분
- 고주파 성분 : 영상에서 픽셀 값이 급격하게 바뀌는 성분

공간적 필터링(Spatial domain filtering)  
- 영상의 픽셀 값을 직접 이용하는 필터링 방법 (대상 좌표의 픽셀 값과 주변 픽셀 값을 동시에 사용)
- 주로 마스크(mask)연산을 이용함(마스크 = 커널(kernel) = 윈도우(window) = 템플릿(template))
- OpenCV에서는 기본적으로 공간적 필터링을 사용하지만 경우에 따라 내부적으로 알아서 주파수 공간에서 필터링을 해준다.

필터링 : 마스크 연산  
- 다양한 모양과 크기의 마스크가 있다.
- 마스크의 형태와 값에 따라 필터의 역할이 결정됨 (e.g. 영상 부드럽게 만들기, 영상 날카롭게 만들기, 에지(edge)검출, 잡음 제거
3x3 크기의 마스크를 이용한 공간적 필터링
- Correlation(Convolution)을 사용한다.  

기본적인 2D필터링  
cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None) -> dst
- src: 입력 영상 (uint8 타입을 자주 사용)
- ddepth: 출력 영상 데이터 타입. (e.g) cv2.CV_8U, cv2.CV_32F, cv2.CV_64F (-1을 지정하면 src와 같은 타입의 dst 영상을 생성)
- kernel: 필터 마스크 행렬. 실수형.
- anchor: 고정점 위치. (-1, -1)이면 필터 중앙을 고정점으로 사용
- delta: 추가적으로 더할 값 (default 값은 0)
- borderType: 가장자리 픽셀 확장 방식
- dst: 출력 영상

## [02 blurring.py : 블러링(1): 평균 값 필터](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch04%20%ED%95%84%ED%84%B0%EB%A7%81/blurring.py)
02 블러링(1): 평균 값 필터

평균 값 필터(Mean filter)  
- 영상의 특정 좌표 값을 주변 픽셀 값들의 산술 평균으로 설정
- 픽셀들 간의 그레이스케일 값 변화가 줄어들어 날카로운 에지가 무뎌지고, 영상에 있는 잡음의 영향이 사라지는 효과
- 영상에 평균 값 필터를 적용할 때 마스크 크기가 커질수록 평균 값 필터 결과가 더욱 부드러워짐(블러 효과가 많이 적용됨) -> 더 많은 연산량 필요!
- 편한 블러링 방식이지만 퀄리티가 떨어지는 단점이 있다. (가우시안 필터가 퀄리티가 더 좋다.)

기본적인 2D필터링  
cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None) -> dst   
- src: 입력 영상 (uint8 타입을 자주 사용)
- ddepth: 출력 영상 데이터 타입. (e.g) cv2.CV_8U, cv2.CV_32F, cv2.CV_64F (-1을 지정하면 src와 같은 타입의 dst 영상을 생성)
- kernel: 필터 마스크 행렬. 실수형.
- anchor: 고정점 위치. (-1, -1)이면 필터 중앙을 고정점으로 사용
- delta: 추가적으로 더할 값 (default 값은 0)
- borderType: 가장자리 픽셀 확장 방식
- dst: 출력 영상

평균 값 필터링 함수  
cv2.blur(src, ksize, dst=None, anchor=None, borderType=None) -> dst  
- src: 입력 영상
- ksize: 평균값 필터 크기. (width, height) 형태의 튜플.
- dst: 결과 영상. 입력 영상과 같은 크기 & 같은 타입.
- kernel = 1 / (ksize.width * ksize.height)
