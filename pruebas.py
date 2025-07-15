import pygame as pg
from figura_class import Rectangulo
pg.init()#Inicializamos los modulos pygame
x_display= 1400
y_display = 900
rectangulo1 = Rectangulo(700,450)
rectangulo1.direccion(0.5, 0.5)


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
    #draw.rect(surface, color en (rgb), posiciones(posicion en x, posicion en y, tamaño x, tamaño en y))
    pg.draw.rect(pantalla,rectangulo1.color,(rectangulo1.x,rectangulo1.y,rectangulo1.width,rectangulo1.height))
    #pg.draw.rect(pantalla,(227, 58, 31),(700,x,40,40))
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()            
