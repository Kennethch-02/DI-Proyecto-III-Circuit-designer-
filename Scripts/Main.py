import pygame
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
    is_running = True
    while is_running:
        pygame.display.update()
        cursor.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        if(cursor.colliderect(pantalla)):
            SCREEN.fill(GREEN)
        else:
            SCREEN.fill(RED)
    pygame.quit()

t = Thread(target=Main())
t.start()