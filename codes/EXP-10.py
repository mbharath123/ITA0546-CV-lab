import cv2
cap = cv2.VideoCapture(0)
delay = 30
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(delay) & 0xFF
    if key == ord('+'):
        delay = max(1, delay - 5)   
    elif key == ord('-'):
        delay += 5                  
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()