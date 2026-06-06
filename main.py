import pygame
import random  # <-- Novo: Importado para gerar posições aleatórias

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Carrinho")

# Configurações do relógio para controlar a velocidade do jogo (FPS)
relogio = pygame.time.Clock()

rodando = True

# Dados do Jogador (Quadrado Vermelho)
carro_x = 375
carro_y = 500
carro_velocidade = 8

# Dados do Obstáculo (Quadrado Azul)
obstaculo_largura = 50
obstaculo_altura = 50
obstaculo_x = random.randint(0, LARGURA - obstaculo_largura) # Posição X aleatória
obstaculo_y = -100  # Começa acima da tela para dar efeito de surgimento
obstaculo_velocidade = 5

while rodando:
    # Garante que o jogo rode a 60 frames por segundo
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 1. CONTROLE DO ELEMENTO PRINCIPAL
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and carro_x > 0:
        carro_x -= carro_velocidade
    if teclas[pygame.K_RIGHT] and carro_x < LARGURA - 50:
        carro_x += carro_velocidade

    # 2. MOVIMENTAÇÃO DO ELEMENTO INTERATIVO (OBSTÁCULO)
    obstaculo_y += obstaculo_velocidade  # Faz o obstáculo descer

    # Se o obstáculo passar do final da tela, ele volta para o topo em um X novo
    if obstaculo_y > ALTURA:
        obstaculo_y = -obstaculo_altura
        obstaculo_x = random.randint(0, LARGURA - obstaculo_largura)

    # 3. DESENHO NA TELA
    tela.fill((50, 50, 50))  # Fundo cinza

    # Desenha o jogador (Vermelho)
    pygame.draw.rect(tela, (255, 0, 0), (carro_x, carro_y, 50, 40))

    # Desenha o obstáculo interativo (Azul)
    pygame.draw.rect(tela, (0, 0, 255), (obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura))

    pygame.display.update()

pygame.quit()