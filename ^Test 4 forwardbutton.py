from tkinter import Tk, Label, Button, PhotoImage


class PhotoViewer:
    def __init__(self):
        self.current_file = None

        self.root = Tk()

        self.label = Label(self.root)
        self.label.pack()

        self.forward_button = Button(self.root, text="Forward", command=self.load_next_photo)
        self.forward_button.pack()

        self.load_next_photo()

        self.root.mainloop()

    def load_next_photo(self):
        next_file = get_next_file(self.current_file)
        self.current_file = next_file
        image = PhotoImage(file=next_file)
        self.label.config(image=image)
        self.label.image = image  # keep a reference to the image to prevent garbage collection


viewer = PhotoViewer()