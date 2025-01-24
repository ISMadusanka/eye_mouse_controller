import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()

while True:
    ret, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks = output.multi_face_landmarks
    print(landmarks)
    if landmarks:
        lm = landmarks[0].landmark

        for l in lm:
            x= l.x
            y= l.y
            print(x, y)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break