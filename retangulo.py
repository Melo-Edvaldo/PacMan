import pygame

pygame.init()

tela = pygame.display.set_mode((640, 480), 0)

VERMELHO = (255, 0, 0)
RETANGULO = (250, 120, 250, 120)

while True:
    # Calcula as regras

    # Pinta
    pygame.draw.rect(tela, VERMELHO, RETANGULO)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()