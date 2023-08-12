import os
import cv2
import numpy as np

# Folder path containing images
folder_path = 'C:\\Setup_code\\unique_screenshots'

# List all files in the folder
image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Parameters for brightness and contrast adjustment
alpha = 1.5  # Contrast control (1.0 is no change)
beta = 50    # Brightness control (0 is no change)

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)

    # Load the image
    image = cv2.imread(image_path)

    # Adjust brightness and contrast
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Save the adjusted image to replace the original image
    cv2.imwrite(image_path, adjusted)

    print(f"Image '{image_file}' adjusted and saved at: {image_path}")
