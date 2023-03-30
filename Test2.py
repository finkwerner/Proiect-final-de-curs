import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class PhotoViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Viewer")
        self.image_list = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]
        self.current_image = 0

        # Create a frame to hold the photo and scrollbar
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas to display the photo
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar to scroll through the images
        self.scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # Load the first image
        self.load_image()

    def load_image(self):
        image_path = self.image_list[self.current_image]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def next_image(self):
        if self.current_image < len(self.image_list) - 1:
            self.current_image += 1
            self.load_image()

    def prev_image(self):
        if self.current_image > 0:
            self.current_image -= 1
            self.load_image()

root = tk.Tk()
app = PhotoViewer(root)
root.mainloop()