import pygame as pg


class Rectangulo:

    def __init__(self, pos_x, pos_y, color=(255, 46,89),w=40, h=40):
        self.color = color
        self.x = pos_x
        self.y = pos_y
        self.width = w
        self.height = h

    def direccion(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def movimiento(self, x_max= 0, y_max = 0):
        self.x += self.vx
        self.y += self.vy

        if self.x == x_max or self.x == 0:
            self.vx = self.vx * -1
        if self.y == y_max or self.y == 0:
            self.vy = self.vy * -1

    def dibujar(self, pantalla):
         pg.draw.rect(pantalla,self.color,(self.x,self.y,self.width,self.height))  
    
class Circulo:
    def __init__(self, pos_x, pos_y, color=(255,255,255), radio=20, vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy

    def movimiento(self, x_max= 0, y_max = 0):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_x == x_max or self.pos_x == 0:
            self.vx = self.vx * -1
        if self.pos_y == y_max or self.pos_y == 0:
            self.vy = self.vy * -1


    def dibujar(self, pantalla):
        pg.draw.circle(pantalla, self.color,(self.pos_x, self.pos_y), self.radio)


        