import subprocess
from string import templatelib
from tkinter import *
from tkinter import messagebox


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Niveles
ANCHO_BLOQUE = 40
FILAS = 10
COLUMNAS = 15
Nivel_actual = 1
avata_x_posicion = 1
avata_y_posicion = 8
avatar_id = None
lienzo = None
ventana_mapa = None
e_nombre = ""
intentos = 0
ventana = None
# Alto = 40*10 = 400
# Ancho = 40*15 = 600

# =========================
# MAPAS
# =========================

MAPAS = {
    1: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,1,0,1,0,0,0,0,0,1],
        [1,0,1,0,0,0,1,0,1,0,0,0,0,0,1],
        [1,0,1,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    2: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,1,1,1,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    3: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,0,0,1],
        [1,0,0,0,0,1,1,0,0,0,0,1,1,1,1],
        [1,0,1,1,0,0,0,0,1,1,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,0,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    4: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,2,1],
        [1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,1,0,1,0,1],
        [1,0,0,0,1,0,1,1,1,0,1,0,1,0,1],
        [1,1,1,1,1,0,1,0,1,0,1,0,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    5: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,1,0,0,0,0,0,0,0,0,0,2,1],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,0,1,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
        [1,1,1,0,1,1,1,0,0,0,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    6: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,0,0,0,2,1],
        [1,0,1,1,1,0,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
        [1,1,1,0,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,1,1,1,1,0,1,0,0,0,1],
        [1,0,1,0,0,0,0,0,1,0,1,1,1,1,1],
        [1,0,0,0,1,1,1,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    7: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
        [1,1,1,1,1,1,1,1,0,1,0,1,1,1,1],
        [1,0,0,0,0,0,0,1,0,1,0,1,0,0,1],
        [1,0,1,1,1,1,0,1,0,1,0,1,0,0,1],
        [1,0,1,0,0,1,0,1,0,0,0,0,0,0,1],
        [1,0,1,0,0,1,0,1,1,1,1,1,1,0,1],
        [1,0,1,1,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    8: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,2,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,1,0,1],
        [1,0,0,0,1,1,1,0,1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    9: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,2,1],
        [1,1,1,1,1,1,1,0,0,1,0,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,1,0,1,0,0,1],
        [1,0,1,1,1,0,1,1,0,1,0,1,0,0,1],
        [1,0,1,0,1,0,0,0,0,1,0,0,0,0,1],
        [1,0,1,0,1,1,0,1,0,1,1,1,1,0,1],
        [1,0,1,0,0,1,0,1,0,0,0,0,1,0,1],
        [1,0,0,0,0,0,0,1,1,1,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ],
    10: [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,1,0,0,0,1,0,0,0,1,0,0,2,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,1,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
        [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
}

# =========================
# FUNCIONES
# =========================


def jugar():
    global e_nombre
    ventana.withdraw()
    ventana_validar = Toplevel()
    ventana_validar.title("Nombre")
    ventana_validar.geometry("400x300")
    ventana_validar.config(bg="#111111")
    lbl_nombre = Label(ventana_validar, text="Ingresa tu nombre:", font=("Arial", 16), bg="#111111", fg="white")
    lbl_nombre.pack(pady=20)
    e_nombre = Entry(ventana_validar, font=("Arial", 16), width=20)
    e_nombre.pack(pady=20)
    def validarNombre():
        if e_nombre.get() == "":
            messagebox.showerror("Error", "Debe ingresar un nombre")
            return
        else:
            # Funcion llamar a las siguiente ventana
            mostrar_niveles()
            ventana_validar.withdraw()
            
    btn_guardar = Button(
        ventana_validar,
        text="Guardar",
        font=("Arial", 16),
        width=20, bg="#2E8B57",
        fg="white", cursor="hand2",
        command=validarNombre
        )
    btn_guardar.pack(pady=20)


def mostrar_instrucciones():
    return


def salir():
    ventana.destroy()


def mostrar_pregunta():
    global Nivel_actual
    with open("./Docs/Preguntas.txt" , "r" , encoding="utf-8") as archivo:
        lista_lineas = archivo.readlines()
        for linea in lista_lineas:
            
            datos = linea.strip().split("|")
            
            num_pregunta = int(datos[0])
            if num_pregunta == Nivel_actual:
            
                pregunta = (datos[1])
                res_correcta = int(datos[5])
                
                break
    
    ventana_pregunta = Toplevel()
    ventana_pregunta.title(f"Pregunta {Nivel_actual}")
    ventana_pregunta.geometry("500x400")
    ventana_pregunta.config(bg="#111111")
    
    lbl_pregunta = Label(
        ventana_pregunta,
        text=pregunta,
        font=("Arial", 16),
        bg="#111111",
        fg="white",
    )
    lbl_pregunta.pack(pady=30)
    
    e_respuesta = Entry(
    ventana_pregunta,
    font=("Arial", 14),
    bd=0,
    width=25,
    justify="center"
    )
    e_respuesta.pack(pady=20)
    

    def comparar():
        """ res_usuario = int(e_respuesta.get()) """
        global avata_x_posicion
        global avata_y_posicion
        global intentos
        try:
            res_usuario = int(e_respuesta.get())
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un numero")
            return
        if res_usuario == res_correcta:
            messagebox.showinfo("Correcto", "Respuesta correcta")
            ventana_pregunta.destroy()
            # Mandar a llamar el siguiente nivel
            cambiar_nivel()
        else:
            intentos += 1
            if intentos < 3:
                messagebox.showerror("Error", f"Respuesta incorrecta vuelva a intentarlo {3-intentos}")
            else:
                mostrar_ventana_perder()
                ventana_pregunta.destroy()
                ventana_mapa.destroy()
                avata_x_posicion = 1
                avata_y_posicion = 8
                intentos = 0
                # Mostrar ventana perdiste   

                return

    btn_enviar = Button(
        ventana_pregunta,
        text="Enviar",
        width=20,
        font=("Arial", 12),
        command=comparar
    )
    btn_enviar.pack(pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_niveles(): 
    global Nivel_actual, avatar_id
    global lienzo
    global ventana_mapa
    ventana_mapa= Toplevel()
    ventana_mapa.title(f"Nivel {Nivel_actual}")
    ventana_mapa.geometry("600x400")
    lienzo = Canvas(
        ventana_mapa,
        width=600,
        height=400,
        bg="#222425"
        )
    lienzo.pack()
    
    mapa = MAPAS[Nivel_actual]
    for fila in range(10):
            for  col in range(15):
                celda = mapa[fila][col]
                
                x1 = col * 40 
                y1 = fila * 40
                x2 = x1 + 40
                y2 = y1 + 40

                # Pared
                if celda == 1:
                    lienzo.create_rectangle(
                        x1, y1,
                        x2, y2,
                        fill="#1A202C",
                        outline="#4A5568",
                        width=1
                    )
                    
                elif celda == 2:
                    lienzo.create_rectangle(
                        x1, y1,
                        x2, y2,
                        fill="#ECC94B",
                        outline="#000000",
                        width=1
                    )
                
                
                # Suelo
                else:
                    lienzo.create_rectangle(
                        x1, y1,
                        x2, y2,
                        fill="#2D3748",
                        outline="#4A5568",
                        width=1
                    )
    """ Creacion del avatar """
    avatar_id = lienzo.create_oval(
        avata_x_posicion * 40 + 5,
        avata_y_posicion * 40 + 5,
        avata_x_posicion * 40 + 35,
        avata_y_posicion * 40 + 35,
        fill="blue",
        outline="black",
        width=2
        )
    
    ventana_mapa.bind("<KeyPress>", teclas)
    ventana_mapa.focus_set()
    
def teclas(event):
    dx = 0
    dy = 0
    if event.keysym=="Up":
        dy = -1 
    elif event.keysym=="Down":
        dy = 1
    elif event.keysym=="Left":
        dx = -1
    elif event.keysym=="Right":
        dx = 1
    if dx != 0 or dy != 0:
        mover_avatar(dx,dy)
    
def mover_avatar(dx, dy):   
    global avata_x_posicion
    global avata_y_posicion
    global avatar_id
    mapa = MAPAS[Nivel_actual]
    nueva_x = avata_x_posicion + dx
    nueva_y = avata_y_posicion + dy
    
    # Choques
    
    if 0 <= nueva_x < 15 and 0 <= nueva_y < 10 and mapa[nueva_y][nueva_x] != 1:
        avata_x_posicion = nueva_x
        avata_y_posicion = nueva_y
        lienzo.move(avatar_id, dx * 40, dy * 40)
        if mapa[nueva_y][nueva_x] == 2:
            mostrar_pregunta()

def cambiar_nivel():
    global Nivel_actual
    global avata_x_posicion
    global avata_y_posicion
    global ventana_mapa
    ventana_mapa.destroy()
    if Nivel_actual == 10:
        mostrar_ventana_ganar()
        Nivel_actual = 1
        avata_x_posicion = 1
        avata_y_posicion = 8
    else:
        Nivel_actual += 1
        avata_x_posicion = 1
        avata_y_posicion = 8
        mostrar_niveles()

def mostrar_ventana_ganar():
    global e_nombre
    nombre = e_nombre.get()
    texto = f"{nombre} ¡¡GANASTE!! 🥳"
    ventana_ganar = Toplevel()
    ventana_ganar.title("¡Ganaste!")
    ventana_ganar.geometry("800x600")
    ventana_ganar.config(bg="#111111")

    trofeo = Label(
        ventana_ganar,
        text="🏆",
        font=("Arial", 120),
        bg="#111111",
        fg="gold"
    )
    trofeo.pack(pady=(40, 10))

    Ganaste = Label(
        ventana_ganar,
        text=texto,
        font=("Arial", 36, "bold"),
        fg="#00ff88",
        bg="#111111"
    )
    Ganaste.pack(pady=10)

    subtitulo = Label(
        ventana_ganar,
        text="Eres increíble 😎🔥",
        font=("Arial", 20),
        fg="white",
        bg="#111111"
    )
    subtitulo.pack(pady=10)

    boton_cerrar = Button(
        ventana_ganar,
        text="Cerrar",
        font=("Arial", 16, "bold"),
        bg="#00cc66",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=ventana_ganar.destroy
    )
    boton_cerrar.pack(pady=40)
    boton_volver_jugar = Button(
        ventana_ganar,
        text="Volver a jugar",
        font=("Arial", 16, "bold"),
        bg="#00cc66",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda: [ventana_ganar.destroy(), ventana_principal()]
    )
    boton_volver_jugar.pack(pady=10)

def mostrar_ventana_perder():
    global e_nombre
    nombre = e_nombre.get()
    texto = f"{nombre} has perdido 💀"
    ventana_perder = Toplevel()
    ventana_perder.title("Perdiste...")
    ventana_perder.geometry("800x600")
    ventana_perder.config(bg="#111111")

    triste = Label(
        ventana_perder,
        text="😔",
        font=("Arial", 120),
        bg="#111111",
        fg="#ff4444"
    )
    triste.pack(pady=(40, 10))

    Perdiste = Label(
        ventana_perder,
        text=texto,
        font=("Arial", 36, "bold"),
        fg="#ff4444",
        bg="#111111"
    )
    Perdiste.pack(pady=10)

    subtitulo = Label(
        ventana_perder,
        text="Mejor suerte para la próxima 👍",
        font=("Arial", 20),
        fg="white",
        bg="#111111"
    )
    subtitulo.pack(pady=10)

    boton_cerrar = Button(
        ventana_perder,
        text="Intentar otra vez",
        font=("Arial", 16, "bold"),
        bg="#ff4444",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda: [ventana_perder.destroy(), ventana_principal()]
    )
    boton_cerrar.pack(pady=40)  

    boton_volver_jugar = Button(
        ventana_perder,
        text="Volver a jugar",
        font=("Arial", 16, "bold"),
        bg="#ff4444",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda: [ventana_perder.destroy(), jugar()]
    )
    boton_volver_jugar.pack(pady=10)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# =========================
# VENTANA PRINCIPAL
# =========================
def ventana_principal():
    global ventana
    ventana = Tk()
    ventana.title("Learn by Escaping")
    ventana.geometry("800x600")
    ventana.config(bg="#111111")
    # Centrar contenido
    titulo = Label(
    ventana,
    text="Learn by Escaping",
        font=("Arial", 32, "bold"),
        fg="white",
        bg="#111111"
    )
    titulo.pack(pady=60)

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
    btn_jugar.pack(pady=20)

    btn_instrucciones = Button(
        ventana,
        text="Instrucciones",
        font=("Arial", 16),
        width=20,
        bg="#4682B4",
        fg="white",
        cursor="hand2",
        command=mostrar_instrucciones
    )
    btn_instrucciones.pack(pady=20)

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
    btn_salir.pack(pady=20)
    ventana.mainloop()


ventana_principal()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCIONES QUE AUN NO VAMOS A USAR
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

def mostrar_ventana_ganar():

    ventana_ganar = Toplevel()
    ventana_ganar.title("¡Ganaste!")
    ventana_ganar.geometry("800x600")
    ventana_ganar.config(bg="#111111")

    trofeo = Label(
        ventana_ganar,
        text="🏆",
        font=("Arial", 120),
        bg="#111111",
        fg="gold"
    )
    trofeo.pack(pady=(40, 10))

    Ganaste = Label(
        ventana_ganar,
        text="¡¡GANASTE!! 🥳",
        font=("Arial", 36, "bold"),
        fg="#00ff88",
        bg="#111111"
    )
    Ganaste.pack(pady=10)

    subtitulo = Label(
        ventana_ganar,
        text="Eres increíble 😎🔥",
        font=("Arial", 20),
        fg="white",
        bg="#111111"
    )
    subtitulo.pack(pady=10)

    boton_cerrar = Button(
        ventana_ganar,
        text="Cerrar",
        font=("Arial", 16, "bold"),
        bg="#00cc66",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=ventana_ganar.destroy
    )
    boton_cerrar.pack(pady=40)





def mostrar_ventana_perder():

    ventana_perder = Toplevel()
    ventana_perder.title("Perdiste...")
    ventana_perder.geometry("800x600")
    ventana_perder.config(bg="#111111")

    triste = Label(
        ventana_perder,
        text="😔",
        font=("Arial", 120),
        bg="#111111",
        fg="#ff4444"
    )
    triste.pack(pady=(40, 10))

    Perdiste = Label(
        ventana_perder,
        text="¡¡PERDISTE!! 💀",
        font=("Arial", 36, "bold"),
        fg="#ff4444",
        bg="#111111"
    )
    Perdiste.pack(pady=10)

    subtitulo = Label(
        ventana_perder,
        text="Mejor suerte para la próxima 👍",
        font=("Arial", 20),
        fg="white",
        bg="#111111"
    )
    subtitulo.pack(pady=10)

    boton_cerrar = Button(
        ventana_perder,
        text="Intentar otra vez",
        font=("Arial", 16, "bold"),
        bg="#ff4444",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=ventana_perder.destroy
    )
    boton_cerrar.pack(pady=40)



"""
