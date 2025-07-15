import pygame as pg
from New_class_figura import Figura
pg.init()#Inicializamos los modulos pygame
x_display= 1400
y_display = 900
rectangulo1 = Figura(700,450)

rectangulo2 = Figura(200,100,(100,100,100))

rectangulo3 = Figura(200,100,(200,222,200))

circulo1 = Figura(200, 500)
circulo2 = Figura(400,300, color=(123,45,90))
circulo3 = Figura(20,600, color=(23,245,190))
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
    rectangulo2.movimiento(x_display,y_display)
    rectangulo3.movimiento(x_display,y_display)
    circulo1.movimiento(x_display, y_display)
    circulo2.movimiento(x_display,y_display)
    circulo3.movimiento(x_display,y_display)
    """
     ESTO ES LO MISNO QUE EL CODIGO DE ABAJO
    #draw.rect(surface, color en (rgb), posiciones(posicion en x, posicion en y, tamaño x, tamaño en y))
    #pg.draw.rect(pantalla,rectangulo1.color,(rectangulo1.x,rectangulo1.y,rectangulo1.width,rectangulo1.height))
    #pg.draw.rect(pantalla,rectangulo2.color,(rectangulo2.x,rectangulo2.y,rectangulo2.width,rectangulo2.height))
    #pg.draw.rect(pantalla,rectangulo3.color,(rectangulo3.x,rectangulo3.y,rectangulo3.width,rectangulo3.height))
    """
    circulo1.dibujar_circulo(pantalla)
    circulo2.dibujar_circulo(pantalla)
    circulo3.dibujar_circulo(pantalla)
    rectangulo1.dibujar_rectangulo(pantalla)
    rectangulo2.dibujar_rectangulo(pantalla)
    rectangulo3.dibujar_rectangulo(pantalla)
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()            