import cv2
def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked at:", x, y)

img = cv2.imread("sample_frame.png")
cv2.imshow("Click to find coordinates", img)
cv2.setMouseCallback("Click to find coordinates", show_coordinates)
cv2.waitKey(0)
cv2.destroyAllWindows()