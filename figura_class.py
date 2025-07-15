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
    
