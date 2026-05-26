from tkinter import *

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
    print("Iniciar juego")

def instrucciones():
    print("Mostrar instrucciones")

def salir():
    ventana.destroy()

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