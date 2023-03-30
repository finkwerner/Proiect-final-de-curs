import os
from tkinter import *

class PhotoViewer:
    def __init__(self, directory):
        self.directory = directory
        self.current_image = None
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.forward_button = Button(self.root, text="Forward", command=self.show_next_image)
        self.forward_button.pack(side=RIGHT)

    def show_next_image(self):
        try:
            self.current_image = next(self.image_generator)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=NW, image=self.current_image)
        except StopIteration:
            pass

    def run(self):
        self.image_generator = self.load_images()
        self.show_next_image()
        self.root.mainloop()

    def load_images(self):
        for filename in sorted(os.listdir(self.directory)):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                yield PhotoImage(file=os.path.join(self.directory, filename))

if __name__ == "__main__":
    viewer = PhotoViewer(directory="path/to/images")
    viewer.run()