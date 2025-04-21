import pygame

pygame.init()

LARGURA = 800
ALTURA = 600

screen = pygame.display.set_mode((LARGURA, ALTURA), 0)
pygame.display.set_caption("Pac Man - Aula 06")

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 0.1

class PacMan:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800 // 30
        self.vel_x = VELOCIDADE
        self.vel_y = VELOCIDADE
        self.raio = self.tamanho // 2

    def calcular_regras(self):
        self.centro_x = self.centro_x + self.vel_x
        self.centro_y = self.centro_y + self.vel_y

        if self.centro_x + self.raio > LARGURA:
            self.vel_x = -VELOCIDADE
        if self.centro_x - self.raio < 0:
            self.vel_x = VELOCIDADE
        if self.centro_y + self.raio > ALTURA:
            self.vel_y = -VELOCIDADE
        if self.centro_y - self.raio < 0:
            self.vel_y = VELOCIDADE
        if __name__ == "__main__":
            pacman = PacMan()

    def pintar(self, tela):
        # Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenho da boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

if __name__ == "__main__":
    pacman = PacMan()

    while True:
        # Calcular as regras
        pacman.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()

        # Captura os eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

# Colocar na inicialização
clk = pygame.time.Clock()

# Colocar dentro do loop
clk.tick(10.0)