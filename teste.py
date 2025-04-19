import pygame

pygame.init()

largura, altura = 640, 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Triângulo Verde")

verde = (0, 255, 0)
branco = (255, 255, 255)

pontos = [(320, 100), (220, 380), (420, 380)]

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(branco)

    pygame.draw.polygon(tela, verde, pontos)

    pygame.display.flip()

pygame.quit()