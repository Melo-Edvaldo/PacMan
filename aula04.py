import pygame

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA), 0)
pygame.display.set_caption("Pac Man - Aula 04")

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)

RAIO = 30

VELOCIDADE = 0.1

x = 10
y = 10

vel_x = VELOCIDADE
vel_y = VELOCIDADE

while True:
    # Calcula as regras
    x = x + vel_x
    y = y + vel_y

    if x + RAIO > LARGURA:
        vel_x = -VELOCIDADE
    if x - RAIO < 0:
        vel_x = VELOCIDADE
    if y + RAIO > ALTURA:
        vel_y = -VELOCIDADE
    if y - RAIO < 0:
        vel_y = VELOCIDADE

    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)
    pygame.display.update()

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()