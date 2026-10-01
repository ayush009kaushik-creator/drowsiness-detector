import cv2
import winsound

camera = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

counter = 0
alarm = False

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    if len(eyes) < 2:
        counter += 1
    else:
        counter = 0
        alarm = False

    if counter > 20:
        cv2.putText(frame,
        "DROWSINESS DETECTED",
        (40,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2)

        winsound.PlaySound("alarm.wav",
       winsound.SND_FILENAME)

        if alarm == False:
            print("ALERT")
            alarm = True

    else:
        cv2.putText(frame,
        "DRIVER ACTIVE",
        (40,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2)

    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Drowsiness Detector", frame)

    if cv2.waitKey(1)==27:
        break

camera.release()
cv2.destroyAllWindows()