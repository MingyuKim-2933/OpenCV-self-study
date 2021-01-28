import cv2
import sys
print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('googlelogo.png', cv2. IMREAD_GRAYSCALE)

if  img is None:
    print('Image load failed!')
    sys.exit()

cv2.imwrite('googlelogogray.png', img)

cv2.namedWindow('image')  # 창 사이즈 조절 가능, 인자로 WiNDOW_AUTOSIZE:창 크기를 영상 크기에 맞게 변경(default), WINDOW_NORMAL:영상 크기를 창 크기에 맞게 지정
cv2.imshow('image', img)

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.destroyAllWindows()  # destroyWindow(): 특정 창만 닫아준다. 