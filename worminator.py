import cv2
import numpy as np
from scipy.signal import find_peaks

# 1. Open the video file
video = cv2.VideoCapture("worm_video.MOV")  # replace with your video file

# 2. This will store the worm head's angle to its own body in every frame
angles = []

# Remembers where the head was in the last frame so we don't lose track of it when the worm reverses
previous_head = None

def get_end_points(contour):
    """Find the two 'ends' of a long thin worm shape."""
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    side_lengths = [np.linalg.norm(box[i] - box[(i + 1) % 4]) for i in range(4)]
    short_side_idx = np.argmin(side_lengths)
    end1 = (box[short_side_idx] + box[(short_side_idx + 1) % 4]) / 2
    end2 = (box[(short_side_idx + 2) % 4] + box[(short_side_idx + 3) % 4]) / 2
    return end1, end2

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
            center = np.array([M["m10"] / M["m00"], M["m01"] / M["m00"]]) 
            end1, end2 = get_end_points(worm)

            # Determine which end is the head (closest to the previous head position)
            if previous_head is None:
                # first frame: just pick one arbitrarily as a starting guess
                head = end1
            else:
                # whichever end is CLOSER to last frame's head, call that the head
                if np.linalg.norm(end1 - previous_head) < np.linalg.norm(end2 - previous_head):
                    head = end1
                else:
                    head = end2

            previous_head = head

            # angle of the head relative to the worm's own center, instead of raw position on the plate
            vector = head - center
            angle = np.arctan2(vector[1], vector[0])
            angles.append(angle)

video.release()

# 4. List of angles
angles = np.array(angles)

# 5. Count how many times it's head touches a peak and trough — each wiggle = one body bend
peaks, _ = find_peaks(angles)
troughs, _ = find_peaks(-angles)
total_bends = len(peaks) + len(troughs)


# 6. Turn that into bends per minute
fps = 30  # frames per second — depends on your video
video_length_seconds = len(angles) / fps
bends_per_minute = total_bends / (video_length_seconds / 60)

print("Bends per minute:", bends_per_minute)

import matplotlib.pyplot as plt

plt.plot(angles)
plt.xlabel("Frame")
plt.ylabel("Head angle")
plt.title("Raw angle signal")
plt.show()
