import pygame as pg
from New_class_figura import Figura
pg.init()#Inicializamos los modulos pygame
x_display= 1400
y_display = 900
rectangulo1 = Figura(700,450)

circulo1 = Figura(200, 500)

# crear pantalla o surface 
pantalla = pg.display.set_mode( (x_display,y_display))# definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame")#agregar titulo a mi ventana

game_over = True
x = 0
vx = 0.5 # Aqui no me funcionaba con 0.3 poruqe entonces el numero de vx nunca llegaba a estar igual que 0 o 1400 porque iba con decimales impares 0.3, 0.6, 0.9. 1,2
while game_over:
    for eventos in pg.event.get():
        print(eventos)#Capturar todos los eventos mientras se ejecuta el bucle
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((50, 189, 172))
    #agregamos objeto a la pantalla
    rectangulo1.movimiento(x_display,y_display)
    circulo1.movimiento(x_display, y_display)
    #draw.rect(surface, color en (rgb), posiciones(posicion en x, posicion en y, tamaño x, tamaño en y))
    rectangulo1.dibujar_rectangulo(pantalla)
    circulo1.dibujar_circulo(pantalla)
    #pg.draw.rect(pantalla,(227, 58, 31),(700,x,40,40))
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()            





