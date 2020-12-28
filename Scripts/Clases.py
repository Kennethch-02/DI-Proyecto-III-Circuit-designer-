import pygame
class Pantalla(pygame.Rect):
    def __init__(self, w, h):
        pygame.Rect.__init__(self, 1, 1, w, h)

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0,0,1,1)
    def update(self):
        pygame.init()
        self.left, self.top = pygame.mouse.get_pos()

class Line:
    def __init__(self, anchura, x, y):
        self.anchura = anchura
        self.x = x
        self.y = y
    def set_anchura(self, anchura):
        self.anchura = anchura
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y