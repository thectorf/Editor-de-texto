from tkinter import *
from tkinter import filedialog as FileDialog
from io import *
ruta = "" # ruta del fichero

def nuevo():
    mensaje.set("Nuevo fichero")
    global ruta # indicamos que la ruta es global
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Primer editor")

def abrir():
    mensaje.set("Abrir fichero")
    global ruta
    ruta = FileDialog.askopenfilename(title = "Abrir un fichero de texto", initialdir = '.', filetype = (("Ficheros de texto", "*.txt"),))
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, "end") # Borrar desde el inicio hasta el final
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - Primer editor")

def guardar():
    mensaje.set("Guardar fichero")
    global ruta
    if ruta != "":
        contenido = texto.get(1.0, "end-1c") # le decimos que guarde desde el inicio hasta el final menos un caracter(que es el salto de linea)
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardarComo()

def guardarComo():
    mensaje.set("Guardar fichero como")
    global ruta
    fichero = FileDialog.asksaveasfile(title = "Guardar fichero", mode = 'w', defaultextension = ".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c") # le decimos que guarde desde el inicio hasta el final menos un caracter(que es el salto de linea)
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Se cancelo el guardado")
        ruta = ""

root = Tk()
root.title("Primer editor")

# Menú superior
menubar = Menu(root)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Nuevo", command = nuevo)
filemenu.add_command(label = "Abrir", command = abrir)
filemenu.add_command(label = "Guardar", command = guardar)
filemenu.add_command(label = "Guardar Como", command = guardarComo)
filemenu.add_separator()
filemenu.add_command(label = "Salir", command = root.quit)
menubar.add_cascade(label = "archivo", menu = filemenu)

#Caja de texto central
texto = Text(root)
texto.pack(fill = "both", expand = 1)
texto.config(bd = 0, padx = 6, pady = 4, font = ("consolas", 12))

#Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar= mensaje, justify = "left")
monitor.pack(side = "left")

root.config(menu = menubar)
root.mainloop()
