import cv2
import numpy as np
import scipy
from scipy.signal import find_peaks

# 1. Open the video
video = cv2.VideoCapture("worm_video.MOV")  # replace with your video file

# 2. This will store the worm's x-position in every frame
positions = []

# 3. Go through the video one frame at a time
while True:
    success, frame = video.read()
    if not success:
        break  # no more frames — video is over

    # Turn the frame black-and-white (easier to work with)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Turn it into pure black/white so the worm stands out from the background
    _, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)

    # Find the outline (contour) of the worm blob
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Assume the biggest blob is the worm
        worm = max(contours, key=cv2.contourArea)
        M = cv2.moments(worm)
        if M["m00"] != 0:
            cx = M["m10"] / M["m00"]  # worm's x-position (center)
            positions.append(cx)

video.release()

# 4. Now we have a list of the worm's x-position, frame by frame.
# As it bends back and forth, this list wiggles up and down.
positions = np.array(positions)

# 5. Count how many times it "wiggles" — each wiggle = one body bend
peaks, _ = find_peaks(positions)

# 6. Turn that into bends per minute
fps = 30  # frames per second — depends on your video
video_length_seconds = len(positions) / fps
bends_per_minute = len(peaks) / (video_length_seconds / 60)

print("Bends per minute:", bends_per_minute)
