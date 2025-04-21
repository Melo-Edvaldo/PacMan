import pygame

pygame.init()

tela = pygame.display.set_mode((640, 480), 0)

VERDE = (0, 255, 0)
TRIANGULO = (320, 100), (220, 380), (420, 380)

while True:
    # Calcula as regras

    # Pinta
    pygame.draw.polygon(tela, VERDE, TRIANGULO, 0)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()