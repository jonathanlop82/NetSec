import Tkinter

root = Tkinter.Tk()
boton = Tkinter.Button(root, text="Minimizar", command=root.iconify)
root.geometry("300x300")
root.maxsize(400, 600)

boton.pack()
root.mainloop()
