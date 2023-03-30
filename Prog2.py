
#https://www.youtube.com/watch?v=Iz5gYUGIz6w
#https://www.youtube.com/watch?v=1650C5uRmCA

import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import os
from tkinter import Label, Button, PhotoImage

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("Jpeg File", "*.jpg"), ("PNG file", "*.png"), ("All file")))
    img=Image.open(filename)

    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img




def get_next_file():
    files = os.listdir(img)

    current_index = files.index
    next_index = current_index + 1 \
        if current_index < len(files) - 1 \
        else 0
    return files[next_index]

root= tkinter.Tk()
fram=Frame(root)
fram.pack(side=LEFT, fill=BOTH, expand=1)




lbl=Label(root)
lbl.pack()


btn=tkinter.Button(fram, text= "Select Image", command=showimage)
btn.place(x=25, y=100)
btn.pack()
btn2=tkinter.Button(fram, text= "Exit", command=lambda:exit())
btn2.pack(padx=100, pady=25)

my_canvas = Canvas(fram)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(fram, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_scrollbar2 = ttk.Scrollbar(fram, orient=HORIZONTAL, command=my_canvas.xview)
my_scrollbar.pack(side=BOTTOM, fill=X)


my_canvas.configure(yscrollcommand=my_scrollbar2.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")


btn_forward= tkinter.Button(fram, text= ">>", command = lambda: get_next_file())


btn_forward.pack(side=tk.LEFT)
btn_forward.pack

root.mainloop()



