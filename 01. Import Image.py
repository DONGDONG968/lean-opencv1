import cv2
img = cv2.imread('image/cat.jpg') # 해당 경로의 파일(이미지) 읽어 오기
cv2.imshow('CAT',img) # img 라는 이름의 창에 CAT 을 표시
cv2.waitKey(0) # 지정된 시간(ms) 동안 사용자 키 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기

###  읽기 옵션 종류 ###
# cv2.IMREAD_COLOR: 컬러 이미지(투명 영역은 무시) (기본값)
# cv2.IMREAD_GRAYSCALE: 흑백 이미지
# cv2.IMREAD_UNCHANGED: 투명 영역까지 포함

# ex) img = cv2.imread('image/cat.jpg', cv2.IMREAD_COLOR)
# ex) img = cv2.imread('image/cat.jpg', cv2.IMREAD_GRAYSCALE)
# ex) img = cv2.imread('image/cat.jpg', cv2.IMREAD_UNCHANGE)