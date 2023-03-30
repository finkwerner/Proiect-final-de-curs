import cv2
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")
        self.current_image_index = 0
        self.image_paths = []

        # Create the UI elements
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.load_button = tk.Button(master, text="Load Image", command=self.load_images)
        self.load_button.pack()

        self.next_button = tk.Button(master, text="Next", command=self.show_next_image)
        self.next_button.pack()

    def load_images(self):
        # Open a file dialog to select the folder containing the images
        folder_path = filedialog.askdirectory()

        # Print the folder path for debugging purposes
        print(f"Selected folder path: {folder_path}")

        # Get a list of all the JPEG, PNG, and RAW images in the folder
        image_extensions = ('.jpg', '.jpeg', '.png', '.raw')
        self.image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
                            if file.lower().endswith(image_extensions)]

        # Print the list of image paths for debugging purposes
        print(f"Found {len(self.image_paths)} image files:")
        for image_path in self.image_paths:
            print(image_path)

        # Show the first image in the folder
        self.show_image(0)

    def show_image(self, index):
        # Load the image and display it on the canvas
        image = cv2.imread(self.image_paths[index])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (400, 400))
        photo = Image.fromarray(image)
        self.canvas.photo = ImageTk.PhotoImage(photo)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.canvas.photo)

        # Update the current image index
        self.current_image_index = index

    def show_next_image(self):
        # Show the next image in the folder
        if self.current_image_index < len(self.image_paths) - 1:
            self.show_image(self.current_image_index + 1)
        else:
            tk.messagebox.showinfo("End of folder", "You have reached the end of the folder")


root = tk.Tk()
viewer = ImageViewer(root)
root.mainloop()