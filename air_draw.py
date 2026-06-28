import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Store drawing points
points = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # mirror view

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 🔴 RED COLOR RANGE (you can adjust later)
    lower_purple = np.array([0, 120, 70])
    upper_purple = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_purple, upper_purple)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # largest red object
        c = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(c)

        # fingertip position (center of box)
        cx = x + w // 2
        cy = y + h // 2

        points.append((cx, cy))

        # draw detection point
        cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)

    # 🎨 DRAW LINES (Air writing)
    for i in range(1, len(points)):
        cv2.line(frame, points[i - 1], points[i], (255, 0, 0), 3)

    cv2.imshow("AirInk - Color Tracking", frame)

    key = cv2.waitKey(1) & 0xFF

    # ESC = exit
    if key == 27:
        break

    # C = clear canvas
    if key == ord('c'):
        points = []

cap.release()
cv2.destroyAllWindows()