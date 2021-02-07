'''
01 기본적인 영상 처리 기법
OpenCV는 영상 데이터를 numpy.ndarray로 표현

ndim: 차원 수. 2 = grayscale, 3 = color, 4 = alpha 값이 포함된 color
shape: 각 차원의 크기. (h, w) 또는 (h, w, 3) 등이 있다.
size: 전체 원소 개수
dtype: 원소의 데이터 타입. 영상 데이터는 uint8(numpy에서 지원하는 데이터타입)

그레이 스케일 영상 : cv2.CV_8UC1 -> numpy.uint8, shape = (h, w)
컬러 영상 : cv2.CV_8UC3 -> numpy.uint8, shape = (h, w, 3)
'''