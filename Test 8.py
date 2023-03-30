import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class ImageViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Simple Image Viewer")
        self.master.geometry("600x600")

        self.top_frame = tk.Frame(self.master, width=600, bd=1, relief="solid")
        self.top_frame.pack(side="top", fill="both", expand="yes")

        self.mid_frame = tk.Frame(self.master, width=300, height=200, bd=1, relief="solid")
        self.mid_frame.pack(side="top")

        self.images = []
        self.location = 0

        self.lbl_title = tk.Label(self.top_frame, text="Label", font=("Arial", 20))
        self.lbl_title.pack()

        self.forward = tk.Button(self.top_frame, text="Forward", command=lambda: self.load_image(1))
        self.forward.pack(side="left")

        self.back = tk.Button(self.top_frame, text="Back", command=lambda: self.load_image(-1))
        self.back.pack(side="left")

        self.parse_folder()

    def parse_folder(self):
        file_path = filedialog.askdirectory()
        if not file_path:
            messagebox.showerror("Error", "No folder selected.")
            return

        try:
            for file in os.listdir(file_path):
                if file.endswith(".jpg") or file.endswith(".png"):
                    self.images.append(os.path.join(file_path, file))
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        if not self.images:
            messagebox.showerror("Error", "No images found in the selected folder.")
            return

        self.load_image(0)

    def load_image(self, direction):
        self.location += direction
        if self.location >= len(self.images):
            self.location = 0
        elif self.location < 0:
            self.location = len(self.images) - 1

        image = Image.open(self.images[self.location])
        image = image.resize((300, 200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        self.lbl_title.config(image=image)
        self.lbl_title.image = image

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()