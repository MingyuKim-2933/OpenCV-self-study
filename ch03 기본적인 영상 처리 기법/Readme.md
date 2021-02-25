# ch03 기본적인 영상 처리 기법

## [01 brightness.py : 영상의 밝기 조절](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/brightness.py)
01 영상의 밝기 조절  

영상의 화소 처리 기법  
화소 처리  
- 입력 영상의 특정 좌표 픽셀 값을 변경하여 출력 영상의 해당 좌표 픽셀 값으로 설정하는 연산  
  dst(x, y) = f(src(x, y))  # f는 변환 함수(transfer function)이다.  
- 결과 영상의 픽셀 값이 정해진 범위(e.g. 그레이스케일)에 있어야 함  
- 반전, 밝기 조절, 명암비 조절 등등  

밝기 조절이란?   
- 영상을 전체적으로 더욱 밝거나 어둡게 만드는 연산  
- 밝기 조절 수식 : dst(x, y) = saturate(src(x, y) + n)  
  saturate 연산 : 영상의 픽셀 값이 255를 넘어가면 255로 제한하고 0 밑으로 내려가면 0으로 제한해주는 연산  
  
영상의 밝기 조절을 위한 영상의 덧셈 연산  
cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst  
- src1: (입력)첫 번째 영상 또는 스칼라  
- src2: (입력)두 번째 영상 또는 스칼라  
- dst: (출력)덧셈 연산의 결과 영상  
- mask: 마스크 영상  
- dtype: 출력 영상(dst)의 타입. (e.g.) cv2.CV_8U, cv2.CV_32F 등  

참고 사항  
- 스칼라는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플  
- dst를 함수 인자로 전달하려면 dst의 크기가 src1, src2와 같아야 하며, 타입이 적절해야함  

## [02 arithmetic.py : 영상의 산술 및 논리 연산](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/arithmetic.py) 
02 영상의 산술 연산  

1) 덧셈 연산  
dst(x, y) = saturate(src1(x, y) + src2(x,y)) # saturate 연산 : 영상의 픽셀 값이 255를 넘어가면 255로 제한하고 0 밑으로 내려가면 0으로 제한해주는 연산  
- 두 영상의 같은 위치에 존재하는 픽셀 값을 더하여 결과 영상의 픽셀 값으로 설정한다.  
- 덧셈 결과가 255보다 크면 픽셀 값을 255로 설정 (포화 연산)  

cv2.add(src1, src2, dst=None, mask=None, dtype=None) -> dst  
- src1: (입력)첫 번째 영상 또는 스칼라  
- src2: (입력)두 번째 영상 또는 스칼라  
- dst: (출력)덧셈 연산의 결과 영상  
- mask: 마스크 영상  
- dtype: 출력 영상(dst)의 타입. (e.g.) cv2.CV_8U, cv2.CV_32F 등 (OpenCV 타입)  

참고 사항  
- 스칼라는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플  
- dst를 함수 인자로 전달하려면 dst의 크기가 src1, src2와 같아야 하며, 타입이 적절해야함  

2) 가중치 합(weighted sum)  
dst(x, y) = saturate(α·src1(x, y) + β·src2(x,y))  
- 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 가중 합을 계산하여 결과 영상의 픽셀 값으로 설정  
- 보통 α + β = 1 이 되도록 설정-> 두 입력 영상의 평균 밝기를 유지  

cv2.add(src1, alpha, src2, beta, gamma, dst=None, dtype=None) -> dst  
- src1: 첫 번째 영상  
- alpha: 첫 번째 영상 가중치  
- src2: 두 번째 영상. src1과 같은 크기 & 같은 타입  
- beta: 두 번째 영상 가중치  
- gamma:  결과 영상에 추가적으로 더할 값  
- dst: 가중치 합 결과 영상  
- dtype: 출력 영상(dst)의 타입. 
 
3) 평균 연산(average)  
dst(x, y) = 1/2(src1(x, y) + src2(x,y))  
- 가중치를 α = β = 0.5로 설정한 가중치 합  

4) 뺄셈 연산  
dst(x, y) = saturate(src1(x, y) - src2(x,y)) # saturate 연산 : 영상의 픽셀 값이 255를 넘어가면 255로 제한하고 0 밑으로 내려가면 0으로 제한해주는 연산  
- 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 뺄셈 연산을 수행하여 결과 영상의 픽셀 값으로 설정한다.  
- 덧셈 결과가 0보다 작으면 픽셀 값을 0으로 설정 (포화 연산)  

cv2.subtract(src1, src2, dst=None, mask=None, dtype=None) -> dst  
- src1: 첫 번째 영상 또는 스칼라  
- src2: 두 번째 영상 또는 스칼라  
- dst: 뺄셈 연산의 결과 영상  
- mask: 마스크 영상  
- dtype: 출력 영상(dst)의 타입. (e.g.) cv2.CV_8U, cv2.CV_32F 등 (OpenCV 타입)  

5) 차이 연산  
dst(x, y) = |src1(x, y) - src2(x, y)|  
- 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 뺄셈 연산을 수행한 후, 그 절댓값을 결과 영상의 픽셀 값으로 설정  
- 뺄셈 연산과 달리 입력 영상의 순서에 영향을 받지 않음  

cv2.absdiff(src1, src2, dst=None) ->dst  
- src1: 첫 번째 영상 또는 스칼라  
- src2: 두 번째 영상 또는 스칼라  
- dst: 차이 연산 결과 영상(차영상)  

6) 영상의 논리 연산  
비트단위 AND, OR, XOR, NOT 연산  
cv2.bitwise_and(src1, src2, dst=None, mask=None) -> dst   
cv2.bitwise_or(src1, src2, dst=None, mask=None) -> dst   
cv2.bitwise_xor(src1, src2, dst=None, mask=None) -> dst  
cv2.bitwise_not(src1, src2, dst=None, mask=None) -> dst  

- src1: 첫 번째 영상 또는 스칼라  
- src2: 두 번째 영상 또는 스칼라  
- dst: 출력 영상  
- mask: 마스크 영상  

참고사항  
- 각각의 픽셀 값을 이진수로 표현하고, 비트(bit)단위 논리 연산을 수행  

## [03 color.py : 컬러 영상과 색 공간](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/color1.py) 
03 컬러 영상과 색 공간

OpenCV와 컬러 영상  
- 컬러 영상은 3차원 numpy.ndarray로 표현. img.shape(h,w,3)  
- OpenCV에서는 RGB순서가 아니라 BGR순서를 기본으로 사용  

RGB 색 공간  
- 빛의 삼원색인 빨간색(R), 녹색(G), 파란색(B)을 혼합하여 색상을 표현(가산 혼합)  
- TV & 모니터, 카메라 센서 Bayer필터, 비트맵  

(색상)채널 분리  
cv2.split(m, mv=None) -> dst  
- m: 다채널 영상(e.g.) (B, G, R)로 구성된 컬러 영상  
- mv: 출력 영상  
- dst: 출력 영상의 리스트  

(색상)채널 결합  
cv2.merge(mv, dst=None) -> dst  # GrayScale 영상 3개가 나온다.  
- mv: 입력 영상 리스트 또는 튜플  
- dst: 출력 영상  

색 공간 변환  
- 영상 처리에서는 특정한 목적을 위해 RGB 색 공간을 HSV, YCrCb, Grayscale 등의 다른 색 공간으로 변환하여 처리  

색 공간 변환 함수  
cv2.cvtColor(src, code, dst=None, dstCn=None) -> dst  
- src: 입력 영상  
- code: 색 변환 코드  # cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2YCrCb 등 (OpenCV 문서 페이지 참고)  
- dstCn: 결과 영상의 채널 수. 0이면 자동 결정.  
- dst: 출력 영상  

RGB 색상을 그레이스케일로 변환  
Y = 0.299R + 0.587G + 0.114B  
- 장점 : 데이터 저장 용량 감소, 데이터 처리 속도 향상  
- 단점 : 색상 정보 손실  

HSV 색 공간  
- Hue: 색상, 색의 종류  
- Saturation: 채도, 색의 탁하고 선명한 정도  
- Value: 명도, 빛의 밝기  
 
HSV값 범위  
cv2.CV_8U 영상의 경우  
- 0<=H<=179  
- 0<=S<=255  
- 0<=V<=255  

YCrCb 색 공간  
- PAL, NTSC, SECAM 등의 컬러 비디오 표준에 사용되는 색 공간  
- 영상의 밝기 정보와 색상 정보를 따로 분리하여 부호화(흑백 TV호환)  
- Y: 밝기 정보(luma)  
- Cr, Cb: 색차(chroma)  

YCrCb값 범위  
cv2.CV_8U 영상의 경우  
- 0<=Y<=255  
- 0<=Cr<=255  
- 0<=Cb<=255  

## [04 histogram.py : 히스토그램 분석](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/histogram.py)
04 히스토그램 분석

히스토그램(Histogram)
- 영상의 픽셀 값 분포를 그래프의 형태로 표현한 것
- 예를 들어 그레이스케일 영상에서 각 그레이스케일 값에 해당하는 픽셀의 개수를 구하고, 이를 막대 그래프의 형태로 표현

정규화된 히스토그램(Normalized histogram)
- 각 픽셀의 개수를 영상 전체 픽셀 개수로 나누어준 것
- 해당 그레이스케일 값을 갖는 픽셀이 나타날 확률

히스토그램 구하기  
cv2.calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None) -> hist
- images: 입력 영상 리스트 (1개의 영상이라도 리스트로 묶어서 입력 값으로 주어야한다.)
- channels: 히스토그램을 구할 채널을 나타내는 리스트
- mask: 마스크 영상. 입력 영상 전체에서 히스토그램을 구하려면 None 지정.
- histSize: 히스토그램 각 차원의 크기(빈(bin)의 개수)를 나타내는 리스트
- ranges: 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
- hist: 계산된 히스토그램 (numpy.ndarray 형태로 반환된다.)
- accumulate: 기존의 hist 히스토그램에 누적하려면 True, 새로 만들려면 False.

## [05 contrast.py : 영상의 명암비 조절](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/contrast.py)
05 영상의 명암비 조절

명암비(Contrast)란?
- 밝은 곳과 어두운 곳 사이에 드러나는 밝기 정도의 차이
- 컨트라스트, 대비
- 명암비가 높으면 밝은 부분과 어두운 부분의 픽셀 값의 차이가 커서 조금 더 선명해보인다.

기본적인 명암비 조절 함수  
dst(x, y) = saturate(s·src(x, y))
- s = 0.5인 경우 : 최대 픽셀 값이 128이라 전체적으로 어두워 진다.
- s = 2인 경우 : 전체적으로 255가 되는 부분이 많아서 하얗게 보이는 부분이 많다.

효과적인 명암비 조절 함수  
dst(x, y) = saturate(src(x, y) + (src(x, y) - 128)·α)
(1 + α) * src(x, y) - 128 * α  # 위의 식과 같다.

히스토그램 스트레칭(Histogram stretching)
- 영상의 히스토그램이 그레이스케일 전 구간에서 걸쳐 나타나도록 변경하는 선형 변환 기법 (양쪽으로 늘려주는 과정에서 중간 중간 픽셀 값이 없는 구간이 생긴다.)

정규화 함수  
cv2.normalize(src, dst, alpha=None, beta, None, norm_type=None, dtype=None, mask=None) -> dst
- src: 입력 영상
- dst: 결과 영상 (스트레칭에서는 None 값으로 주면 된다.)
- alpha: (노름 정규화인 경우) 목표 노름 값, (원소 값 범위 정규화인 경우) 최솟값
- beta: (원소 값 범위 정규화인 경우) 최댓값
- norm_type: 정규화 타입. NORM_INF, NORM_L1, NORM_L2, NORM_MINMAX.  # NORM_MINMAX를 선택한 후 alpha에 0 beta에 255를 대입한다.
- dtype: 결과 영상의 타입
- mask: 마스크 영상

히스토그램 스트레칭 변환 함수  
(f(x, y) -G(min)) / (G(max) - G(min)) * 255  # 변환 함수의 직선의 방정식

## [06 equalize.py : 히스토그램 평활화](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/equalize.py)
06 히스토그램 평활화

히스토그램 평활화(Histogram equalization)  
- 히스토그램이 그레이스케일 전체 구간에서 균일한 분포로 나타나도록 변경하는 명암비 향상 기법
- 히스토그램 균등화, 균일화, 평탄화

히스토그램 평활화를 위한 변환 함수 구하기  
- 변환 함수 : dst(x, y) = round(cdf(src(x, y)) * L(max))  # 누적 분포 함수(cdf)를 사용해서 구한다.

히스토그램 평활화  
cv2.equalizeHist(src, dst=None) -> dst
- src: 입력 영상. 그레이스케일 영상
- dst: 결과 영상

컬러 히스토그램 평활화  
- 직관적 방법: R, G, B 각 색 평면에 대해 히스토그램 평활화  
- (입력)컬러 영상 -> (R,G,B) plane 분할 -> 각각 히스토그램 평활화 -> merge -> (출력)컬러 영상  # 이 방법은 색감이 바껴 좋지 않아 이렇게 하면 안된다.  
- (입력)컬러 영상 -> (Y,Cr,Cb) plane 분할 -> Y값만 히스토그램 평활화 -> merge -> (출력)컬러 영상  # 색감은 유지되면서 명암비만 증가되어 원하는 결과를 얻을 수 있다.

## [07 inrange.py : 특정 색상 영역 추출](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/inrange.py)
07 특정 색상 영역 추출

RGB 색 공간에서 특정 색상 영역을 추출하기 보다 HSV, YCrCb 공간에서 특정 색상 영역 추출을 많이한다.

HSV 색 공간에서 녹색 영역 추출하기
- H(Hue): 색상의 종류 (색상) (0 ~ 179)
- S(Saturation): 색상의 채도 (선명도) (0 ~ 255) (어느정도 값을 높게 설정해야한다. ex.150 < S < 255)
- V(Value): 색상의 명도 (밝기) (0 ~ 255)

특정 범위 안에 있는 행렬 원소 검출
cv2.inRange(src, lowerb, upperb, dst=None) -> dst (mask 영상: 0 또는 255로만 구성된 이진 영상)
- src: 입력 행렬
- lowerb: 하한 값 행렬 또는 스칼라
- upperb: 상한 값 행렬 또는 스칼라
- dst: 입력 영상과 같은 크기의 마스크 영상. 범위 안에 들어가는 픽셀은 255, 나머지는 0으로 설정. (numpy.uint8)

## [08 backproj.py : 히스토그램 역투영](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/backproj.py)
08 히스토그램 역투영

히스토그램 역투영(Histogram backprojection)
- 영상의 각 픽셀이 주어진 히스토그램 모델에 얼마나 일치하는지를 검사하는 방법
- 임의의 색상 영역을 검출할 때 효과적(inrange 함수보다 임의의 색상 영역을 검출한다. e.x. 살색)
- YCrCb 컬러 스페이스와 LAB를 많이 쓴다.

히스토그램 역투영을 이용한 살색 검출
1) 기준 영상으로부터 살색에 대한 컬러 히스토그램을 미리 계산
2) 입력 영상에서 미리 구한 살색 히스토그램에 부합하는 픽셀을 선별

히스토그램 역투영 함수  
cv2.calcBackProject(images, channels, hist, ranges, scale, dst=None) -> dst
- images: 입력 영상 리스트
- channels: 역투영 계산에 사용할 채널 번호 리스트
- hist: 입력 히스토그램(numpy.ndarray)
- ranges: 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
- scale: 출력 역투영 행렬에 추가적으로 곱할 값
- dst: 출력 역투영 영상. 입력 영상과 동일 크기, cv2.CV_8U.

## [09 chroma_key.py : 크로마 키 합성](https://github.com/MingyuKim-2933/OpenCV-self-study/blob/main/ch03%20기본적인%20영상%20처리%20기법/chroma_key.py)
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
