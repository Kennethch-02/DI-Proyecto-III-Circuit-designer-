import pygame
import sys
from Clases import *
from threading import Thread

#/____________________________________________________________________________________________________________________
#/_________________________________________Funciones__________________________________________________________________

def Main():
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
    cursor1 = cursor()

#/____________________________________________________________________________________________________________________
#/_________________________________________VENTANA INDICACIONES_______________________________________________________

    def Indicaciones ():
        #Variables de la ventana
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
        #Variables del Boton
        boton_a2= pygame.image.load("./boton_atras.gif")
        boton_a3 = pygame.image.load ("./boton_atras.gif")
        boton_atras = boton(boton_a3,boton_a2,590,400) #cambia la posicion del boton
        cursor1 = cursor()
        #Ciclo de la ventana
        while salir != True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton_atras.rect):
                        return main()
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

# /____________________________________________________________________________________________________________________
# /_________________________________________VENTANA INDICACIONES_______________________________________________________

    def Simulador ():
        #Variables de la ventana
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
        #Variables del boton
        boton_as1 = pygame.image.load ("./boton_atras.gif")
        boton_as2 = pygame.image.load("./boton_atras.gif")
        boton_atras_sim = boton(boton_as1,boton_as2,590,400) #cambia la posicion del boton
        cursor1 = cursor()
        #ciclo de la ventana
        while salir != True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cursor1.colliderect(boton_atras_sim.rect):
                        return main()
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
                    return Simulador()

        #actualizaciones e impresiones del trabajo
        pantalla.fill(colorfondo)
        pantalla.blit(texto, (220,70))
        cursor1.update()
        boton1.update(pantalla, cursor1)
        boton2.update(pantalla, cursor1)
        pygame.display.update()
    pygame.quit()

t = Thread(target=Main)
t.start()