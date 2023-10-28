#testing repository
#circle detection placeholder for actual colab file

import cv2
import numpy as np

def detect_black_circles(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Check if image loaded successfully
    if img is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    blurred = cv2.medianBlur(gray, 5)

    # Detect circles using Hough transform
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT, dp=1,
        minDist=20, param1=50,
        param2=30, minRadius=5,
        maxRadius=150
    )

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            # draw the circle in the output image
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            # draw a rectangle corresponding to the center of the circle
            cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

        plt.imshow("Detected Circles", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("No circles were detected")
    
    return #necessity of this?

image = 'metal_some_covered.jpg'  # Assuming the image is in the same directory and has a .jpg extension
detect_black_circles(image)
