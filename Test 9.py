from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Image Viewer")

size = (900, 900)
defaultFolder = r"C:\Users\finkw\Desktop\Budapest gute"

path = filedialog.askdirectory (initialdir=defaultFolder, title="Select Image Folder")

print(path)

imageExtension = ("png", "jpeg", "jpg", "gif")

imageList = [file for file in os.listdir(path) if file.endswith(imageExtension)]

img = Image.open(path + "/" + imageList[0])
img.thumbnail(size)

img.show()

labelImage = ImageTk.PhotoIMage(img)
rootLabel = Label(image=labelImage)


rootLabel.grid(row=0, column=0, columnspan=3)

def prevFn():
    global cnt
    global img
    global rootLabel

    rootLabel.grid_forget()

    prevButton.grid_forget()
    nextButton.grid_forget()
    exitButton.grid_forget()


    cnt += 1

    if cnt > len(imageList):
        cnt = Len(imageList) - 1
    img = Image.open(path+"/"+ìmageList[cnt])
    img.thumbnail(size)
    labelIMage = ImageTK.PhotoImage(img)
    rootLabel = Label(image=labelImage)

    rootLabel.img = labelImage
    prevButton.grid(row=1, column=0)
    nextButton.grid(row=1, column=2)
    exitButton.grid(row=1, column=1)

    rootLabel.grid(row=0, column=0, columnspan=3)

def nextFn():
    pass

prevButton = Button(root, text="<<", command=prevFn)
nextButton = Button(root, text=">>", command=nextFn)
exitButton = Button(root, text="Exit()", command=root.quit)

prevButton.grid(row=1, column=0)
nextButton.grid(row=1, column=2)
exitButton.grid(row=1, column=1)

print(imageList)



root.mainloop