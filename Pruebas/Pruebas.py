from tkinter import *

# =========================
# VENTANA PRINCIPAL
# =========================

ventana = Tk()
ventana.title("Juego")
ventana.geometry("500x400")



# =========================
# VENTANA GANAR
# =========================

def mostrar_ventana_ganar():

    ventana_ganar = Toplevel()
    ventana_ganar.title("¡Ganaste!")
    ventana_ganar.geometry("800x600")
    ventana_ganar.config(bg="#111111")
    ventana_ganar.resizable(False, False)

    # Emoji/Trofeo
    trofeo = Label(
        ventana_ganar,
        text="🏆",
        font=("Arial", 120),
        bg="#111111",
        fg="gold"
    )
    trofeo.pack(pady=(40, 10))

    # Texto principal
    Ganaste = Label(
        ventana_ganar,
        text="¡¡GANASTE!! 🥳",
        font=("Arial", 36, "bold"),
        fg="#00ff88",
        bg="#111111"
    )
    Ganaste.pack(pady=10)

    # Subtítulo
    subtitulo = Label(
        ventana_ganar,
        text="Eres increíble 😎🔥",
        font=("Arial", 20),
        fg="white",
        bg="#111111"
    )
    subtitulo.pack(pady=10)

    # Botón cerrar
    boton_cerrar = Button(
        ventana_ganar,
        text="Cerrar",
        font=("Arial", 16, "bold"),
        bg="#00cc66",
        fg="white",
        activebackground="#00ff88",
        activeforeground="black",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=ventana_ganar.destroy
    )
    boton_cerrar.pack(pady=40)


# =========================
# VENTANA PERDER
# =========================

def mostrar_ventana_perder():

    ventana_perder = Toplevel()
    ventana_perder.title("Perdiste...")
    ventana_perder.geometry("800x600")
    ventana_perder.config(bg="#111111")
    ventana_perder.resizable(False, False)

    # Emoji triste
    triste = Label(
        ventana_perder,
        text="😔",
        font=("Arial", 120),
        bg="#111111",
        fg="#ff4444"
    )
    triste.pack(pady=(40, 10))

    # Texto principal
    Perdiste = Label(
        ventana_perder,
        text="¡¡PERDISTE!! 💀",
        font=("Arial", 36, "bold"),
        fg="#ff4444",
        bg="#111111"
    )
    Perdiste.pack(pady=10)

    # Subtítulo
    subtitulo = Label(
        ventana_perder,
        text="Mejor suerte para la próxima 👍",
        font=("Arial", 20),
        fg="white",
        bg="#111111"
    )
    subtitulo.pack(pady=10)

    # Botón cerrar
    boton_cerrar = Button(
        ventana_perder,
        text="Intentar otra vez",
        font=("Arial", 16, "bold"),
        bg="#ff4444",
        fg="white",
        activebackground="#ff6666",
        activeforeground="black",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=ventana_perder.destroy
    )
    boton_cerrar.pack(pady=40)


# =========================
# BOTONES PRINCIPALES
# =========================

titulo = Label(
    ventana,
    text="SIMULADOR DE RESULTADO"
)
titulo.pack(pady=40)

btn_ganar = Button(
    ventana,
    text="Ganar",
    command=mostrar_ventana_ganar
)
btn_ganar.pack(pady=20)

btn_perder = Button(
    ventana,
    text="Perder",
    command=mostrar_ventana_perder
)
btn_perder.pack(pady=20)



ventana.mainloop()