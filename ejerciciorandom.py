import random as ra

import pygame as pg
from New_class_figura import Figura
pg.init()#Inicializamos los modulos pygame
x_display= 1400
y_display = 900


# crear pantalla o surface 
pantalla = pg.display.set_mode( (x_display,y_display))# definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame")#agregar titulo a mi ventana

circulos_random=[]
rectangulos_random=[]

for i in range(1,101):
    circulos_random.append(Figura(ra.randint(0,x_display),ra.randint(0, y_display), (ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)), radio=ra.randint(1,20)))
    rectangulos_random.append(Figura(ra.randint(0,x_display),ra.randint(0, y_display), (ra.randint(0,255),ra.randint(0,255),ra.randint(0,255)), w=ra.randint(1,40), h=ra.randint(1,40)))
game_over = True

while game_over:
    for eventos in pg.event.get():
        print(eventos)#Capturar todos los eventos mientras se ejecuta el bucle
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((50, 189, 172))

    for i in circulos_random:
        i.movimiento(x_display,y_display)
        i.dibujar_circulo(pantalla)
    for i in rectangulos_random:
        i.movimiento(x_display, y_display)
        i.dibujar_rectangulo(pantalla)    


    
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()            