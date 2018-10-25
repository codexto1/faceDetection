from tkinter import *

def create_window():
    window = Toplevel(root)

root = Tk()
b = Button(root, text="Create new window", command=create_window)
b.pack()

root.mainloop()
