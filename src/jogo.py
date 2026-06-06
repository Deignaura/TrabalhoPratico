import pygame

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
    CINZA, VERMELHO, AZUL, BRANCO,
    LARGURA_CARRO, ALTURA_CARRO,
    LARGURA_OBSTACULO, ALTURA_OBSTACULO,
    VELOCIDADE_CARRO, VELOCIDADE_OBSTACULO,
    CAMINHO_RECORDE,
)
from src.funcoes import (
    mover_jogador,
    mover_obstaculo,
    reiniciar_obstaculo,
    verificar_colisao,
    calcular_pontos,
    jogador_perdeu,
)
from src.dados import salvar_recorde, carregar_recorde


def desenhar_carro(tela, x, y):
    """Desenha o carro do jogador na tela."""
    pygame.draw.rect(tela, VERMELHO, (x, y, LARGURA_CARRO, ALTURA_CARRO))


def desenhar_obstaculo(tela, x, y):
    """Desenha o obstáculo na tela."""
    pygame.draw.rect(tela, AZUL, (x, y, LARGURA_OBSTACULO, ALTURA_OBSTACULO))


def desenhar_hud(tela, fonte, pontos, recorde, vidas):
    """Exibe pontuação, recorde e vidas no canto superior da tela."""
    texto = fonte.render(
        f"Pontos: {pontos}  |  Recorde: {recorde}  |  Vidas: {vidas}",
        True, BRANCO
    )
    tela.blit(texto, (10, 10))


def executar_jogo():
    """Executa o loop principal do jogo de carrinho."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, 30)

    carro_x = LARGURA_TELA // 2 - LARGURA_CARRO // 2
    carro_y = ALTURA_TELA - ALTURA_CARRO - 20

    obstaculo_x, obstaculo_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)

    pontos = 0
    vidas = 3
    recorde = carregar_recorde(CAMINHO_RECORDE)
    rodando = True

    while rodando:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()
        carro_x = mover_jogador(
            carro_x,
            teclas[pygame.K_LEFT],
            teclas[pygame.K_RIGHT],
            VELOCIDADE_CARRO,
            LARGURA_TELA,
            LARGURA_CARRO,
        )

        obstaculo_y = mover_obstaculo(obstaculo_y, VELOCIDADE_OBSTACULO)

        if obstaculo_y > ALTURA_TELA:
            obstaculo_x, obstaculo_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)
            pontos = calcular_pontos(pontos)

        carro_rect     = pygame.Rect(carro_x, carro_y, LARGURA_CARRO, ALTURA_CARRO)
        obstaculo_rect = pygame.Rect(obstaculo_x, obstaculo_y, LARGURA_OBSTACULO, ALTURA_OBSTACULO)

        if verificar_colisao(carro_rect, obstaculo_rect):
            vidas -= 1
            obstaculo_x, obstaculo_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)

        if jogador_perdeu(vidas):
            rodando = False

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        tela.fill(CINZA)
        desenhar_carro(tela, carro_x, carro_y)
        desenhar_obstaculo(tela, obstaculo_x, obstaculo_y)
        desenhar_hud(tela, fonte, pontos, recorde, vidas)
        pygame.display.flip()

    pygame.quit()
