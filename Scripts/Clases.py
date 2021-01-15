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

class Cursor_sprite(pygame.sprite.Sprite):
    def __init__(self, cursor):
        pygame.init()
        self.rect = cursor
        self.rect.topleft = pygame.mouse.get_pos()

class Line(pygame.Rect):
    def __init__(self,x,y,w,h):
        pygame.Rect.__init__(self, x,y,w,h)
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def set_x(self, x):
        self.left = x
    def set_y(self, y):
        self.top = y
    def set_pos(self, pos):
        self.left, self.top = pos

class Line_(pygame.sprite.Sprite):
    def __init__(self,surface, color , x,y,w,h):
        pygame.sprite.Sprite.__init__(self)
        self.line = Line(x,y,w,h)
        self.color = color
        self.surface = surface
        self.rect = pygame.rect
    def Draw(self):
        self.rect = pygame.draw.rect(self.surface, self.color, self.line)
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def set_x(self, x):
        self.line.set_x(x)
    def set_y(self, y):
        self.line.set_y(y)
    def set_pos(self,pos):
        self.line.set_pos(pos)
    def get_rect(self):
        return self.line

#/____________________________________________________________________________________________________________________
#/_________________________________________Clases_____________________________________________________________________

class cursor (pygame.Rect):#Solo es un rectangulo que sigue al cursor
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):#actualiza constantemente la posicion
        self.left, self.top = pygame.mouse.get_pos()

class boton(pygame.sprite.Sprite):#tiene dos imagenes que seran el boton
    def __init__(self, imagen1, imagen2, x=300, y=70):
        self.imagen_normal = imagen1
        self.imagen_selec = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.topleft = (x,y)
    def update(self, pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_selec
        else: self.imagen_actual = self.imagen_normal
        pantalla.blit (self.imagen_actual, self.rect)