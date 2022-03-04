from tkinter import *
# from PIL import ImageTk, Image
NAME = "Electrical Bill"
root = Tk()
root.geometry("1000x500")
root.minsize(1000, 500)
root.title(NAME)
title = Label(root, text=NAME, font=("Arial Bold", 30))
title.pack()
photo = PhotoImage('xyz.png')
l = Label(image = photo)
l.pack()

root.mainloop()