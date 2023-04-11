import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

font = cv2.FONT_HERSHEY_SIMPLEX

def colorToAscii(color):
    gray_scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"'.\t\t\t\t\t"

    scale_factor = round(255 / len(gray_scale))
    index = round(color / scale_factor)

    return gray_scale[len(gray_scale) - index - 1]

def convert(frame):
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = []
    for h in range(height):
        for w in range(width):
            r, g, b = frame[h][w]
            brightness = round((r+g+b)/3)
            frame[h][w] = (brightness, brightness, brightness)
    return frame

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # img = np.zeros((height, width, 3), np.uint8)

    new_frame = convert(frame)

    # for i in range(0, width, 10):
    #     x = int(i/10)
    #     cv2.putText(img, ascii_frame[x],
    #                 (0, x*3),
    #                 font, 0.1,
    #                 (255, 255, 255),
    #                 1, 2)


    cv2.imshow("Stanler", new_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()