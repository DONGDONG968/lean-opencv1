import cv2
cap = cv2.VideoCapture('image/video.mp4')

while cap.isOpened(): # 동영상 파일이 올바로 열렸는지?
    ret, frame = cap.read() # ret : 성공여부, frame : 받아온 이미지(프레임)
    if not ret:
        print('더 이상 가져올 프레임이 없어요')
        break
    
    cv2.imshow('video', frame)

    if cv2.waitKey(25) == ord('q'):
        print('사용자 입력에 의해 종료 합니다')
        break

cap.release() # 자원 해제
cv2.destroyAllWindow() 