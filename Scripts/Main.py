import pygame
import sys
from Clases import *
from threading import Thread

def Main():
    pygame.init()
    WIDTH = 500
    HEIGHT = 400
    cursor = Cursor()
    pantalla = Pantalla(WIDTH-2, HEIGHT-2)
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('My Game')

    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 255)

    line = Line_(SCREEN, BLACK, 10, 10, 100, 5)
    Lista = pygame.sprite.Group()
    Lista.add(line)
    is_running = True
    is_down = False
    SCREEN.fill(GREEN)
    # /_____________________________________________________________________________________________________________
    # /_________________________________________CODIGO MONTSE_______________________________________________________

    # /_____________________________________________________________________________________________________________
    # /_________________________________________Clases______________________________________________________________

    class cursor(pygame.Rect):  # Solo es un rectangulo que sigue al cursor
        def __init__(self):
            pygame.Rect.__init__(self, 0, 0, 1, 1)

        def update(self):  # actualiza constantemente la posicion
            self.left, self.top = pygame.mouse.get_pos()

    class boton(pygame.sprite.Sprite):  # tiene dos imagenes que seran el boton
        def __init__(self, imagen1, imagen2, x=300, y=70):
            self.imagen_normal = imagen1
            self.imagen_selec = imagen2
            self.imagen_actual = self.imagen_normal
            self.rect = self.imagen_actual.get_rect()
            self.rect.topleft = (x, y)

        def update(self, pantalla, cursor):
            if cursor.colliderect(self.rect):
                self.imagen_actual = self.imagen_selec
            else:
                self.imagen_actual = self.imagen_normal
            pantalla.blit(self.imagen_actual, self.rect)


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
    cursor1 = cursor()

    # /_________________________________________________________________________________________________________________
    # /_________________________________________VENTANA INDICACIONES____________________________________________________

    def Indicaciones():
        # Variables de la ventana
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
        cursor1 = cursor()
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
            cursor1.update()
            boton_atras.update(pantalla, cursor1)
            pygame.display.update()
        Indicaciones()

        # /_____________________________________________________________________________________________________________
        # /_________________________________________VENTANA SIMULADOR___________________________________________________

        def Simulador():
            # Variables de la ventana
            pygame.init()
            pantalla = pygame.display.set_mode([800, 600])
            pygame.display.set_caption('Inicio')
            salir = False
            blanco = (255, 255, 255)
            negro = (0, 0, 0)
            rojo = (200, 0, 0)
            colorfondo = blanco
            fuente = pygame.font.SysFont("Javanese text", 45)
            texto = fuente.render("Simula", True, negro)  # Texto de bienvenida
            # Variables del boton
            boton_as1 = pygame.image.load("./boton_atras.gif")
            boton_as2 = pygame.image.load("./boton_atras.gif")
            boton_atras_sim = boton(boton_as1, boton_as2, 590, 400)  # cambia la posicion del boton
            cursor1 = cursor()
            # ciclo de la ventana
            while salir != True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if cursor1.colliderect(boton_atras_sim.rect):
                            return Main()
                    elif event.type == pygame.QUIT:
                        salir = True
                        sys.exit()

                # actualizaciones e impresiones del trabajo
                pantalla.fill(colorfondo)
                pantalla.blit(texto, (340, 40))  # Texto de bienvenida
                cursor1.update()
                boton_atras_sim.update(pantalla, cursor1)
                pygame.display.update()
            Simulador()


    while is_running:
        pygame.display.update()
        cursor.update()
        SCREEN.fill(GREEN)
        for e in Lista:
            e.Draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_down = True
                a = pygame.sprite.spritecollide(Cursor_sprite(cursor), Lista, False, False)
                print(a)
                if cursor1.colliderect(boton1.rect):
                    return Indicaciones()
                elif cursor1.colliderect(boton2.rect):
                    return Simulador()
            if event.type == pygame.MOUSEBUTTONUP:
                is_down = False
        if is_down:
            for sprite in a:
                sprite.set_pos(pygame.mouse.get_pos())

    pantalla.fill(colorfondo)
    pantalla.blit(texto, (220, 70))
    cursor1.update()
    boton1.update(pantalla, cursor1)
    boton2.update(pantalla, cursor1)
    pygame.display.update()
    pygame.quit()

t = Thread(target=Main)
t.start()