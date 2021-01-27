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
    def get_x(self):
        return self.left
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
    def update(self):

        self.Draw()
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
        self.active_cable = False
        self.cursor = pygame.image.load("./C_Cable.png")
        self.cursor_active = pygame.image.load("./C_Cable_A.png")
        self.cursor = pygame.transform.scale(self.cursor,(50,50))
        self.cursor_active = pygame.transform.scale(self.cursor_active,(50,50))
    def update(self, pantalla):#actualiza constantemente la posicion
        self.left, self.top = pygame.mouse.get_pos()
        if self.active_cable:
            self.top -= 50
            pantalla.blit(self.cursor, self)
    def cable_cursor(self, pantalla):
        pygame.mouse.set_visible(False)
        self.active_cable = True
    def normal_cursor(self):
        pygame.mouse.set_visible(True)
        self.active_cable = False

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

class Dynamic_Button(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x, y,scale_x,scale_y, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image_normal = pygame.transform.scale(image1,(self.scale_x,self.scale_y))
        self.image_select = pygame.transform.scale(image2,(self.scale_x,self.scale_y))
        self.image_current = self.image_normal
        self.rect = self.image_current.get_rect()
        self.rect.topleft = (x,y)

    def update(self, screen, cursor):
        if cursor.colliderect(self.rect):
            self.image_current = self.image_select
        else:
            self.image_current = self.image_normal
        screen.blit(self.image_current,self.rect)
    def get_type(self):
        return self.type


class Bar_Menu():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rows = 0
        self.col = 0
        self.this_row = 0
        self.Botones = pygame.sprite.Group()
        self.rect = pygame.rect.Rect(x,y,800,100)
        self.IMG_B_Up = pygame.image.load("./arrow_up.png")
        self.IMG_B_up = pygame.image.load("./arrow_u.png")
        self.IMG_B_Down = pygame.image.load("./arrow_down.png")
        self.IMG_B_down = pygame.image.load("./arrow_d.png")
        self.B_Up = Dynamic_Button(self.IMG_B_Up, self.IMG_B_up, 775, 0, 25,25, "null")
        self.B_Down = Dynamic_Button(self.IMG_B_Down, self.IMG_B_down, 775, 75, 25,25, "null")

    def add_button(self, button):
        if self.col > 7:
            self.col = 0
        self.rows = len(self.Botones)//8
        pos_x = self.col*75 + 25
        pos_y = 25
        if self.rows > 0:
            pos_y = -150
        button.rect.topleft = (pos_x,pos_y)
        self.Botones.add(button)
        self.col += 1

    def update(self, pantalla, cursor):
        self.Botones.update(pantalla, cursor)
        self.B_Up.update(pantalla, cursor)
        self.B_Down.update(pantalla, cursor)
        pygame.draw.rect(pantalla, (0, 0, 0), self.rect, 1)

    def show_row(self):
        cont = 0
        for sprite in self.Botones:
            if self.this_row == cont//8:
                sprite.rect.top = 25
            else:
                sprite.rect.top = -150
            cont+=1

    def event(self, event, cursor):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor.colliderect(self.B_Up.rect):
                if(self.this_row > 0):
                    self.this_row-=1
                    self.show_row()
            if cursor.colliderect(self.B_Down.rect):
                if (self.this_row < self.rows):
                    self.this_row += 1
                    self.show_row()

class Resistance(pygame.sprite.Sprite):
    def __init__(self, Ohm, input_voltage,image,x,y,scale_x,scale_y):
        pygame.sprite.Sprite.__init__(self)
        self.Ohm = Ohm
        self.input_voltage = input_voltage
        self.output_voltage = self.Ohm * self.input_voltage
        self.image = image
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = pygame.transform.scale(image, (self.scale_x, self.scale_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.is_down = False
    def update(self, screen, cursor):
        if self.is_down:
            self.rect.center = pygame.mouse.get_pos()
        screen.blit(self.image, self.rect)
    def move_sprite(self,event,cursor):
        if cursor.colliderect(self.rect):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(self.rect):
                    self.rotate()
                self.is_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_down = False
    def rotate(self):
        self.image = pygame.transform.rotate(self.image, 90)

class Batery(pygame.sprite.Sprite):
    def __init__(self, voltage, image, x, y, scale_x, scale_y):
        pygame.sprite.Sprite.__init__(self)
        self.voltage = voltage
        self.image = image
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = pygame.transform.scale(image, (self.scale_x, self.scale_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.is_down = False
    def update(self, screen, cursor):
        if self.is_down:
            self.rect.center = pygame.mouse.get_pos()
        screen.blit(self.image, self.rect)
    def move_sprite(self, event, cursor):
        if cursor.colliderect(self.rect):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_down = False
    def rotate(self):
        return 0


