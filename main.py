import pygame as pg

pg.init()



# crear pantalla o surface 

pantalla = pg.display.set_mode( (1400,900))# definicion de tamaño de pantalla
pg.display.set_caption( "Intro Pygame")#agregar titulo a mi ventana

game_over = True
x = 0
vx = 0.3
while game_over:
    for eventos in pg.event.get():
        print(eventos)#Capturar todos los eventos mientras se ejecuta el bucle
        if eventos.type == pg.QUIT:
            game_over = False
    pantalla.fill((50, 189, 172))
    #agregamos objeto a la pantalla
    x += vx
    if x == 1400 or x== 0:
        vx = vx * -1
    x
    #draw.rect(surface, color en (rgb), posiciones(posicion en x, posicion en y, tamaño x, tamaño en y))
    pg.draw.rect(pantalla,(227, 58, 31),(x,900-40,40,40))
    pg.display.flip()#funcion para cargar toda la configuracion que va dentro de la pantalla

pg.quit()            
