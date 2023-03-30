btn_back = Button(root, text="<<")
btn_foreward = Button(root, text=">>")


def batch_resize():
  for k, v in flags.items():
    v = Image.open(v).resize((WIDTH, HEIGHT), Image.ANTIALIAS)
    flags[k] = ImageTk.PhotoImage(v)
