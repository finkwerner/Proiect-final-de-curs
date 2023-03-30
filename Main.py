import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog


def open_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        print(f"Error: Could not open image {image_path}")
        return

    # Display the image using OpenCV
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def select_image():
    # Open a file dialog to select an image
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=(("JPEG Files", "*.jpeg"),
                   ("PNG Files", "*.png"),
                   ("RAW Files", "*.raw"),
                   ("All Files", "*.*"))
    )
    # Open the selected image
    if file_path:
        open_image(file_path)


# Create a Tkinter window with a button to select images
root = tk.Tk()
root.title("Image Viewer")
button = tk.Button(root, text="Select Image", command=select_image)
button.pack()
root.mainloop()

