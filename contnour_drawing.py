import cv2
import numpy as np

cap = cv2.VideoCapture(0)

points = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)

        # ignore small noise
        if cv2.contourArea(c) > 3000:

            x, y, w, h = cv2.boundingRect(c)

            cx = x + w // 2
            cy = y + h // 2

            points.append((cx, cy))

            cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)

    # draw lines
    for i in range(1, len(points)):
        cv2.line(frame, points[i - 1], points[i], (255, 0, 0), 3)

    cv2.imshow("AirInk Contour Mode", frame)
    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC
        break

    if key == ord('c'):
        points = []

cap.release()
cv2.destroyAllWindows()