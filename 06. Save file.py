import cv2
img = cv2.imread('image/cat.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기
cv2.imshow('CAT',img) # img 라는 이름의 창에 CAT 을 표시
cv2.waitKey(0) # 지정된 시간(ms) 동안 사용자 키 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기

result = cv2.imwrite('cat_save.jpg',img)
print(result)