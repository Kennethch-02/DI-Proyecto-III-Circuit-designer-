from datetime import datetime
import pygame
import os
#Clase pantalla, la cual se encarga de pintar en el lienzo
class Pantalla(pygame.Rect):
    def __init__(self, w, h):
        pygame.Rect.__init__(self, 1, 1, w, h)
#Clase cursor la cual sonsiste en un rectangulo transparente que sigue al cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0,0,1,1)
    def update(self):
        pygame.init()
        self.left, self.top = pygame.mouse.get_pos()
#Clase Curso_Sprite se encarga del funcionamiento de la interaccion del cursor
class Cursor_sprite(pygame.sprite.Sprite):
    def __init__(self, cursor):
        pygame.init()
        self.rect = cursor
        self.rect.topleft = pygame.mouse.get_pos()
#Clase linea se encarga de dibujar las lineas que serán los cables en todas las posiciones posibles
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
#Clase line_ se encarga de pintar dicha linea
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
    # Setea posiciones
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
#Clase encargada de cada caja de texto que se encuentre en la interfaz
class text_box(pygame.sprite.Sprite):
    def __init__(self, x,y,w,h, text):
        pygame.sprite.Sprite.__init__(self)
        self.y = y
        self.input = pygame.Rect(x,self.y,w,h)
        self.h = h
        self.w = w
        self.color_i = (0, 0, 0)
        self.color_a = (255, 255, 255)
        self.color = self.color_i
        self.active = False
        self.text = text
        self.txt = ""
#Actualiza parametros
    def update(self, screen, cursor, dynamic,xy):
        font = pygame.font.Font("times.ttf", 18)
        self.txt = font.render(self.text, True, (0, 0, 0))
        if dynamic:
            width = max(100, self.txt.get_width() + 10)
            self.input.w = width
        self.input.topleft = xy
        self.input.x -= 15
        self.input.y += 15
        pygame.draw.rect(screen, self.color, self.input, 1)
        screen.blit(self.txt, (self.input.x + 1, self.input.y + 1))
#actualiza el texto
    def text_update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input.collidepoint(event.pos):
                # Set the value of the variable
                self.active = not self.active
            else:
                self.active = False
            # Set the current color of the box
            self.color = self.color_a if self.active else self.color_i
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def edit_text(self, text):
        self.text = text

    def get_text(self):
        return self.text
#Solo es un rectangulo que sigue al cursor
class cursor (pygame.Rect):
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
#tiene dos imagenes que seran el boton
class boton(pygame.sprite.Sprite):
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
#Realiza el boton dinamico en lugar de estatico
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
#Clase encargada del menú de la interfaz
class Bar_Menu():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rows = 0
        self.col = 0
        self.this_row = 0
        self.Botones = pygame.sprite.Group()
        self.rect = pygame.rect.Rect(x,y,1000,100)
        self.IMG_B_Up = pygame.image.load("./arrow_up.png")
        self.IMG_B_up = pygame.image.load("./arrow_u.png")
        self.IMG_B_Down = pygame.image.load("./arrow_down.png")
        self.IMG_B_down = pygame.image.load("./arrow_d.png")
        self.B_Up = Dynamic_Button(self.IMG_B_Up, self.IMG_B_up, 975, 0, 25,25, "null")
        self.B_Down = Dynamic_Button(self.IMG_B_Down, self.IMG_B_down, 975, 75, 25,25, "null")

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
#Clase que se comportará como la resistencia de la interfaz
class Resistance(pygame.sprite.Sprite):
    def __init__(self, Ohm, input_voltage,image,x,y,scale_x,scale_y, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.Ohm = Ohm
        self.name = ""
        self.input_voltage = input_voltage
        self.output_voltage = self.Ohm * self.input_voltage
        self.image = image
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = pygame.transform.scale(image, (self.scale_x, self.scale_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.is_down = False
        self.is_rotate = False
        self.name_box = text_box(self.rect.x, self.rect.y, 50, 25, "Name")
        self.Ohm_box = text_box(self.rect.right, self.rect.bottom, 50, 25, "Ohm")
        if self.Ohm != 0:
            self.Ohm_box.edit_text(str(self.Ohm))

    def update(self, screen, cursor):
        if self.is_down:
            self.rect.center = pygame.mouse.get_pos()
        if cursor.colliderect(self.rect):
            self.name_box.update(screen, cursor, False, self.rect.topleft)
            self.Ohm_box.update(screen, cursor, False, (self.rect.right-30, self.rect.bottom-45))
        screen.blit(self.image, self.rect)
        self.name = self.name_box.get_text()
        self.Ohm = self.Ohm_box.get_text()

    def move_sprite(self,event,cursor):
        self.name_box.text_update(event)
        self.Ohm_box.text_update(event)
        if cursor.colliderect(self.rect):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(self.rect):
                    self.rotate()
                self.is_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_down = False
    def rotate(self):
        if self.is_rotate:
            self.image = pygame.transform.rotate(self.image, 270)
            self.is_rotate = False
        else:
            self.image = pygame.transform.rotate(self.image, 90)
            self.is_rotate = True

    def set_name(self, name):
        self.name = name
        self.name_box.edit_text(self.name)
#Clase bateria con sus atributos respectivos
class Batery(pygame.sprite.Sprite):
    def __init__(self, voltage, image, x, y, scale_x, scale_y, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.voltage = voltage
        self.image = image
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image = pygame.transform.scale(image, (self.scale_x, self.scale_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.is_down = False
        self.is_rotate = False
        self.voltage_box = text_box(self.rect.x, self.rect.y, 25, 25, "V")
        if voltage != 0:
            self.voltage_box.edit_text(str(self.voltage))
    def update(self, screen, cursor):
        if self.is_down:
            self.rect.center = pygame.mouse.get_pos()
        self.voltage_box.update(screen, cursor, False, self.rect.topleft)
        screen.blit(self.image, self.rect)
        self.voltage = self.voltage_box.get_text()
    def move_sprite(self, event, cursor):
        self.voltage_box.text_update(event)
        if cursor.colliderect(self.rect):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(self.rect):
                    self.rotate()
                self.is_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.is_down = False
    def rotate(self):
        if self.is_rotate:
            self.image = pygame.transform.rotate(self.image, 270)
            self.is_rotate = False
        else:
            self.image = pygame.transform.rotate(self.image, 90)
            self.is_rotate = True
#Clase encargada de generar el circuito
class Circuito():
    def __init__(self, screen):
        self.Elements = pygame.sprite.Group()
        self.Lines = pygame.sprite.Group()
        self.IMG_F_P = pygame.image.load("./F_P.PNG")
        self.IMG_R = pygame.image.load("./R.PNG")
        self.screen = screen
    #Se encarga de guarfar el circuito en el netlist file
    def Save_Circuit(self):
        count_txt = 0
        content = os.listdir()
        for archive in content:
            if archive.endswith(".txt"):
                count_txt += 1
        time = datetime.now()
        name = "SAVE_" + str(count_txt)
        # name.split(" ", 10)
        Archive = open(name + ".txt", "w")
        for sprite in self.Elements:
            info = ""
            if sprite.type == "batery":
                info += sprite.type + ","
                info += str(sprite.voltage) + ","
                info += str(sprite.rect.x) + ","
                info += str(sprite.rect.y)
                info += "\n"
            if sprite.type == "resistance":
                info += sprite.type + ","
                info += str(sprite.name) + ","
                info += str(sprite.Ohm) + ","
                info += str(sprite.rect.x) + ","
                info += str(sprite.rect.y)
                info += "\n"
            Archive.write(info)
        for line in self.Lines:
            info = ""
            info += "line,"
            info += str(line.line.x) + ","
            info += str(line.line.y) + ","
            info += str(line.line.width) + ","
            info += str(line.line.height)
            info += "\n"
            Archive.write(info)
        Archive.close()
    #Recarga el circuito guardado
    def Load_Circuit(self, name):
        self.Lines.empty()
        self.Elements.empty()
        Archive = open(name + ".txt", "r")
        stri = Archive.read()
        stri = stri.split("\n")
        matrix = []
        for line in stri:
            matrix.append(line.split(","))
        for element in matrix:
            print(element)
            if element[0] == 'batery':
                batery = Batery(int(element[1]),self.IMG_F_P ,int(element[2]),int(element[3]), 100, 100, "batery")
                self.Elements.add(batery)
            if element[0] == 'resistance':
                resistance = Resistance(float(element[2]), 0,self.IMG_R, int(element[3]),int(element[4]),100,100, "resistance")
                resistance.set_name(element[1])
                self.Elements.add(resistance)
            if element[0] == 'line':
                line = Line_(self.screen, (0, 0, 0), int(element[1]),int(element[2]),int(element[3]),int(element[4]))
                self.Lines.add(line)
        Archive.close()