from tkinter import *
from tkinter import messagebox

# =========================
# VENTANA PRINCIPAL
# =========================
ventana = Tk()
ventana.title("Learn by Escaping")
ventana.geometry("800x600")
ventana.config(bg="#111111")

# Centrar contenido
ventana.columnconfigure(0, weight=1)

# =========================
# FUNCIONES
# =========================
def jugar():
    nombre = PedirNombre(ventana)
def instrucciones():
    print("Mostrar instrucciones")

def salir():
    ventana.destroy()

def PedirNombre(ventana_padre):
    global nombre
    ventana2 = Toplevel(ventana_padre)
    ventana2.title("Nombre")
    ventana2.geometry("400x300")
    ventana2.config(bg="#111111")
    nombre = Entry(ventana2, font=("Arial", 16), width=20)
    nombre.pack(pady=20)
    def validarNombre():
        if nombre.get() == "":
            messagebox.showerror("Error", "Debe ingresar un nombre")
            ventana2.destroy()
            return
        else:
            """ Funcion para empezar a jugar """
    btn_guardar = Button(ventana2, text="Guardar", font=("Arial", 16), width=20, bg="#2E8B57", fg="white", cursor="hand2", command=validarNombre)
    btn_guardar.pack(pady=20)

# =========================
# TITULO
# =========================
titulo = Label(
    ventana,
    text="Learn by Escaping",
    font=("Arial", 32, "bold"),
    fg="white",
    bg="#111111"
)

titulo.grid(row=0, column=0, pady=60)

# =========================
# BOTON JUGAR
# =========================
btn_jugar = Button(
    ventana,
    text="Jugar",
    font=("Arial", 16),
    width=20,
    bg="#2E8B57",
    fg="white",
    cursor="hand2",
    command=jugar
)

btn_jugar.grid(row=1, column=0, pady=10)

# =========================
# BOTON INSTRUCCIONES
# =========================
btn_instrucciones = Button(
    ventana,
    text="Instrucciones",
    font=("Arial", 16),
    width=20,
    bg="#4682B4",
    fg="white",
    cursor="hand2",
    command=instrucciones
)

btn_instrucciones.grid(row=2, column=0, pady=10)

# =========================
# BOTON SALIR
# =========================
btn_salir = Button(
    ventana,
    text="Salir",
    font=("Arial", 16),
    width=20,
    bg="#B22222",
    fg="white",
    cursor="hand2",
    command=salir
)

btn_salir.grid(row=3, column=0, pady=10)

# =========================
# EJECUTAR
# =========================
ventana.mainloop()