from tkinter import *
from PIL import ImageTk
screen = Tk()
photo0 = ImageTk.PhotoImage(file = r"C:\Users\finkw\Desktop\Budapest gute\DSC_4673.JPG")
photo1 = ImageTk.PhotoImage(file = r"C:\Users\finkw\Desktop\Budapest gute\DSC_4675.JPG")
photo2 = ImageTk.PhotoImage(file = r"C:\Users\finkw\Desktop\Budapest gute\DSC_4676.JPG")

photo = [photo0, photo1, photo2]
imagenr = 0
#background

l = Label(screen, image= photo [imagenr])
l.grid()
def forward():
    global l, imagenr
    print(l)
    imagenr = imagenr + 1
    l.grid_forget()
    l = Label(screen, image = photo[imagenr])
    l.grid
    b1 = Button(screen, text=">>", command=forward)
    b1.place(x=1100, y=600)
    b2 = Button(screen, text="<<", command = backward)
    b2.place(x=70, y=600)

def backward():
    global l, imagenr
    l.grid_forget()
    l = label(screen, image = photo[imagenr])
b1 = Button(screen, text=">>", command=forward)
b1.place(x=1100, y=600)
b2 = Button(screen, text="<<", command = backward)
b2.place(x=70, y=600)
screen.mainloop()