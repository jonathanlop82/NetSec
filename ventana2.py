#!/usr/bin/env python

import Tkinter as tk

root = tk.Tk()
root.title("MyScan")
# Creamos una ventana hija de root
#otra_ventana = Tkinter.Toplevel(root)
#otra_ventana.title("Ventana hija")
# Este es solo para decoracion
#etiqueta = Tkinter.Label(otra_ventana, text='Este es un ejemplo de transient')
#etiqueta.pack()
# Posicionamos las dos ventanas para que sea mas claro el ejemplo
#root.geometry("400x400+100+100")
#otra_ventana.geometry("200x200+150+150")
# Y ahora si llamamos a este metodo
#otra_ventana.transient(root)


#bop = tk.Frame()
#bop.pack(side=tk.LEFT)

tex = tk.Text(master=root)
tex.pack(side=tk.TOP)
bop = tk.Frame()
bop.pack(side=tk.BOTTOM)


s = 'Prueba'
tex.insert(tk.END, s)
tex.see(tk.END)


tk.Button(bop, text='Exit', command=root.destroy).pack()
root.mainloop()
