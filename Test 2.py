from tkinter import *

from PIL import ImageTk, Image

root=Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('c:/gui/codemy.ico')

my_img = ImageTK.PhotoImage(Image.open("images/aspen.png"))
my_label = Label(image=my_img)
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()