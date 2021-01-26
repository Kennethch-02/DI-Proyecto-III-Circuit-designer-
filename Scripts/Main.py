import sys

import pygame
from Clases import *

##Variables globales
cursor1 = cursor()
#/____________________________________________________________________________________________________________________
#/_________________________________________Funciones__________________________________________________________________

#/____________________________________________________________________________________________________________________
#/_________________________________________VENTANA INDICACIONES_______________________________________________________
def Indicaciones():
    # Variables de la ventana
    global cursor1
    pygame.init()
    pantalla = pygame.display.set_mode([800, 600])
    pygame.display.set_caption('Inicio')
    salir = False
    blanco = (255, 255, 255)
    negro = (0, 0, 0)
    rojo = (200, 0, 0)
    colorfondo = blanco
    fuente = pygame.font.SysFont("Javanese text", 45)
    texto = fuente.render("Indicaciones", True, negro)  # Texto de bienvenida
    # Variables del Boton
    boton_a2 = pygame.image.load("./boton_atras.gif")
    boton_a3 = pygame.image.load("./boton_atras.gif")
    boton_atras = boton(boton_a3, boton_a2, 590, 400)  # cambia la posicion del boton

    # Ciclo de la ventana
    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton_atras.rect):
                    return Main()
            if event.type == pygame.QUIT:
                salir = True
                sys.exit()
        # actualizaciones e impresiones del trabajo
        pantalla.fill(colorfondo)
        pantalla.blit(texto, (270, 50))  # Texto de bienvenida
        cursor1.update(pantalla)
        boton_atras.update(pantalla, cursor1)
        pygame.display.update()
    pygame.quit()
    #Indicaciones()
# /____________________________________________________________________________________________________________________
# /_________________________________________VENTANA SIMULADOR__________________________________________________________
def Simulador():
    global cursor1
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    #Pantalla = Pantalla(WIDTH - 2, HEIGHT - 2)
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('My Game')

    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 255)

    boton_a2 = pygame.image.load("./boton_atras.gif")
    boton_a3 = pygame.image.load("./boton_atras.gif")
    IMG_B_Up = pygame.image.load("./arrow_up.png")
    IMG_B_up = pygame.image.load("./arrow_u.png")
    IMG_F_P = pygame.image.load("./F_P.PNG")
    IMG_R = pygame.image.load("./R.PNG")
    boton_atras = boton(boton_a3, boton_a2, 590, 400)  # cambia la posicion del boton

    line = Line_(pantalla, BLACK, 10, 400, 100, 5)
    Lista = pygame.sprite.Group()
    Lista.add(line)
    Elements = pygame.sprite.Group()
    is_running = True
    is_down = False
    draw_line = False
    Lines = pygame.sprite.Group()
    coord_line = (0,0)
    menu = Bar_Menu(0,0)
    pantalla.fill(GREEN)
    B_F_P = Dynamic_Button(IMG_F_P, IMG_F_P, 25, 25, 60,60, "B_F_P")
    B_Res = Dynamic_Button(IMG_R, IMG_R, 25, 25, 60, 60, "B_Res")
    menu.add_button(B_F_P)
    menu.add_button(B_Res)
    while is_running:
        pantalla.fill(WHITE)
        cursor1.update(pantalla)
        Lista.update()
        Lines.update()
        menu.update(pantalla, cursor1)
        Elements.update(pantalla, cursor1)
        boton_atras.update(pantalla, cursor1)
        for sprite in Lista:
            sprite.Draw()
        pygame.display.update()
        for event in pygame.event.get():
            menu.event(event, cursor1)
            for s in Elements:
                s.move_sprite(event, cursor1)
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for s in menu.Botones:
                    if cursor1.colliderect(s.rect):
                        if s.get_type() == "B_F_P":
                            print("Colocar fuente de poder")
                            cursor1.cable_cursor(pantalla)
                        if s.get_type() == "B_Res":
                            resistence = Resistance(1, 1, IMG_R, 200, 200, 100, 100)
                            Elements.add(resistence)
                            cursor1.normal_cursor()
                is_down = True
                if cursor1.active_cable:
                    coord_line = pygame.mouse.get_pos()
                    draw_line = True
                    lines = Line_(pantalla, BLACK, coord_line[0], coord_line[1], 1,1)
                    Lines.add(lines)
                a = pygame.sprite.spritecollide(Cursor_sprite(cursor1), Lista, False, False)
                print(a)
                if cursor1.colliderect(boton_atras.rect):
                    cursor1.normal_cursor()
                    return Main()
            if event.type == pygame.MOUSEBUTTONUP:
                is_down = False
                if cursor1.active_cable:
                    draw_line = False
        if is_down:
            for sprite in a:
                sprite.set_pos(pygame.mouse.get_pos())
        if draw_line:
            coord = pygame.mouse.get_pos()
            print(coord[0]-coord_line[0])
            if((coord[0]-coord_line[0])<0):
                print("Hola")
                print(lines.line.get_x())
                lines.line.set_x((coord[0]-coord_line[0])+lines.line.get_x())
                lines.line.set_width(-1*(coord[0] - coord_line[0]))
            else:
                lines.line.set_width(coord[0]-coord_line[0])
    pygame.quit()
    #Simulador()

def Main():
    global cursor1
    #Variables Ventana
    pygame.init()
    pantalla = pygame.display.set_mode([800,600])
    pygame.display.set_caption('Inicio')
    salir = False
    blanco = (255,255,255)
    negro = (0,0,0)
    rojo = (200,0,0)
    colorfondo = blanco
    fuente = pygame.font.SysFont("Javanese text",55)
    texto = fuente.render("Circuit Designer", True, negro)#Texto de bienvenida
    #variables para el boton
    boton_ind1 = pygame.image.load ("./boton_ind1.gif")
    boton_ind2 = pygame.image.load("./boton_ind1.gif")
    boton_sim1 = pygame.image.load("./boton_sim1.gif")
    boton_sim2 = pygame.image.load("./boton_sim1.gif")
    boton1 = boton(boton_ind1,boton_ind2)
    boton2 = boton(boton_sim1, boton_sim2,300,120)

# /____________________________________________________________________________________________________________________
# /_________________________________________VENTANA INDICACIONES_______________________________________________________
# /____________________________________________________________________________________________________________________
# /_________________________________________Ciclo Main_________________________________________________________________

    while salir != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    return Indicaciones()
                elif cursor1.colliderect(boton2.rect):
                    return  Simulador()

        #actualizaciones e impresiones del trabajo
        pantalla.fill(colorfondo)
        pantalla.blit(texto, (220,70))
        cursor1.update(pantalla)
        boton1.update(pantalla, cursor1)
        boton2.update(pantalla, cursor1)
        pygame.display.update()
    pygame.quit()

#t = Thread(target=Main)
#t.start()
Main()