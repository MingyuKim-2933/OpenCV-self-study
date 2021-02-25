'''
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
'''
import cv2,sys

img =cv2.imread('img/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
# while True: -- 이렇게 코드를 작성하면 waitKey()를 두번 호출하여 원하는 동작을 하지 않는다.
#     if cv2.waitKey() == 27:
#         break
#     if cv2.waitKey() == ord('i'):
#         img = ~img  # ~ 연산자는 영상처리에서 반전을 준다.

while True:
    key = cv2.waitKey()  # cv2.waitKey를 담는 변수를 사용하여 코드를 작성해야 한다.
    if key == 27:
        break
    if key == ord('i'):
        img = ~img
        cv2.imshow('image', img)

cv2.destroyAllWindows()