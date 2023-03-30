import tkinter

master = tkinter.Tk()
master.title("Place")
master.geometry("400x450")

button1 = tkinter.Button(master, text= "button1")
button1.place(x=25, y=100)

button2=tkinter.Button(master, text="button2")
button2.place(x=100, y=25)

master.mainloop()