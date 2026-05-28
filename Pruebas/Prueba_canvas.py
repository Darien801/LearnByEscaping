from tkinter import *

ANCHO_BLOQUE = 40
FILAS = 5
COLUMNAS = 5

    # Ancho = 40*5 = 200
    # Alto = 40*5 = 200





ventana= Tk()
canvas = Canvas(
        ventana,
        width=200,
        height=200,
        bg="#222425"
    )
canvas.pack()



    # 1 = suelo
    # 0 = pared

MAPA = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ]

def dibujar_mapa():
        for fila in range(5):
            for  col in range(5):
                celda = MAPA[fila][col]
                x1 = col * ANCHO_BLOQUE
                y1 = fila * ANCHO_BLOQUE

                x2 = x1 + ANCHO_BLOQUE
                y2 = y1 + ANCHO_BLOQUE

                # Pared
                if celda == 1:
                    canvas.create_rectangle(
                        x1, y1,
                        x2, y2,
                        fill="gray"
                    )

                # Suelo
                else:
                    canvas.create_rectangle(
                        x1, y1,
                        x2, y2,
                        fill="white"
                    )

dibujar_mapa()
ventana.mainloop()
