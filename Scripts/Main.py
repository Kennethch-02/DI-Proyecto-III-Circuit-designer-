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

    line = Line_(SCREEN, BLACK, 10, 10, 100, 5)
    Lista = pygame.sprite.Group()
    Lista.add(line)
    is_running = True
    is_down = False
    SCREEN.fill(GREEN)
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
            if event.type == pygame.MOUSEBUTTONUP:
                is_down = False
        if is_down:
            for sprite in a:
                sprite.set_pos(pygame.mouse.get_pos())
    pygame.quit()

t = Thread(target=Main)
t.start()