import pygame

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
    CINZA, VERMELHO, AZUL, BRANCO, AMARELO, VERDE, PRETO,
    LARGURA_CARRO, ALTURA_CARRO,
    LARGURA_OBSTACULO, ALTURA_OBSTACULO,
    RAIO_MOEDA,
    VELOCIDADE_CARRO, VELOCIDADE_OBSTACULO_BASE,
    AUMENTO_VELOCIDADE, PONTOS_POR_NIVEL,
    PONTOS_MOEDA, VIDAS_INICIAIS,
    CAMINHO_RECORDE, CAMINHO_RANKING, TAMANHO_RANKING,
)
from src.funcoes import (
    mover_jogador,
    mover_obstaculo,
    reiniciar_obstaculo,
    verificar_colisao,
    calcular_pontos,
    jogador_perdeu,
    calcular_velocidade,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking,
)
from src.sons import inicializar_som


def _desenhar_carro(tela, x, y):
    """Desenha o carro do jogador na tela com detalhes."""
    pygame.draw.rect(tela, VERMELHO, (x, y, LARGURA_CARRO, ALTURA_CARRO))
    pygame.draw.rect(tela, (180, 0, 0), (x + 8, y + 6, LARGURA_CARRO - 16, ALTURA_CARRO - 14))


def _desenhar_obstaculo(tela, x, y):
    """Desenha o obstáculo na tela com detalhes."""
    pygame.draw.rect(tela, AZUL, (x, y, LARGURA_OBSTACULO, ALTURA_OBSTACULO))
    pygame.draw.rect(tela, (0, 40, 160), (x + 8, y + 8, LARGURA_OBSTACULO - 16, ALTURA_OBSTACULO - 16))


def _desenhar_moeda(tela, cx, cy):
    """Desenha a moeda colecionável."""
    pygame.draw.circle(tela, AMARELO, (cx, cy), RAIO_MOEDA)
    pygame.draw.circle(tela, (200, 160, 0), (cx, cy), RAIO_MOEDA - 5)


def _desenhar_hud(tela, fonte, pontos, recorde, vidas, tempo_s):
    """Exibe a pontuação, recorde, vidas e tempo na tela."""
    texto = fonte.render(
        f"Pontos: {pontos}  |  Recorde: {recorde}  |  Vidas: {vidas}  |  Tempo: {tempo_s}s",
        True, BRANCO,
    )
    tela.blit(texto, (10, 10))


def _desenhar_pista(tela, offset):
    """Desenha marcações de pista com efeito de rolagem para simular movimento."""
    offset_int = int(offset) % 80
    # Bordas laterais da pista
    pygame.draw.rect(tela, BRANCO, (28, 0, 6, ALTURA_TELA))
    pygame.draw.rect(tela, BRANCO, (LARGURA_TELA - 34, 0, 6, ALTURA_TELA))
    # Linha central tracejada que rola para baixo
    for y in range(-80 + offset_int, ALTURA_TELA + 80, 80):
        pygame.draw.rect(tela, (160, 160, 160), (LARGURA_TELA // 2 - 5, y, 10, 40))



def _tela_nome(tela, relogio, fonte_grande, fonte_pequena):
    """Tela inicial que captura o nome do jogador. Retorna None se fechar a janela."""
    nome = ""
    while True:
        relogio.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome.strip():
                    return nome.strip()
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                elif len(nome) < 15 and evento.unicode.isprintable() and evento.unicode != " " * len(evento.unicode):
                    nome += evento.unicode

        tela.fill(PRETO)

        titulo = fonte_grande.render("TURBO ESCAPE", True, AMARELO)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 130))

        sub = fonte_pequena.render("Desvie dos obstáculos e colete moedas!", True, BRANCO)
        tela.blit(sub, (LARGURA_TELA // 2 - sub.get_width() // 2, 210))

        instrucao = fonte_pequena.render("Digite seu nome e pressione ENTER:", True, (180, 180, 180))
        tela.blit(instrucao, (LARGURA_TELA // 2 - instrucao.get_width() // 2, 290))

        cursor = "_" if (pygame.time.get_ticks() // 500) % 2 == 0 else " "
        caixa = fonte_grande.render(nome + cursor, True, AMARELO)
        tela.blit(caixa, (LARGURA_TELA // 2 - caixa.get_width() // 2, 335))

        dica = fonte_pequena.render("Setas / A-D: mover   |   ESC: sair", True, (120, 120, 120))
        tela.blit(dica, (LARGURA_TELA // 2 - dica.get_width() // 2, 430))

        pygame.display.flip()


def _tela_fim(tela, relogio, fonte_grande, fonte_pequena, venceu, pontos, recorde, nome):
    ranking = carregar_ranking(CAMINHO_RANKING, TAMANHO_RANKING)

    while True:
        relogio.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    return False

        tela.fill(PRETO)

        if venceu:
            msg = fonte_grande.render("VOCÊ VENCEU!", True, VERDE)
        else:
            msg = fonte_grande.render("GAME OVER", True, VERMELHO)
        tela.blit(msg, (LARGURA_TELA // 2 - msg.get_width() // 2, 40))

        info = fonte_pequena.render(
            f"Pontuação final: {pontos}   |   Recorde: {recorde}", True, BRANCO
        )
        tela.blit(info, (LARGURA_TELA // 2 - info.get_width() // 2, 115))

        titulo_rank = fonte_pequena.render("─── RANKING ───", True, AMARELO)
        tela.blit(titulo_rank, (LARGURA_TELA // 2 - titulo_rank.get_width() // 2, 165))

        for i, (n, p) in enumerate(ranking):
            cor = AMARELO if n == nome else BRANCO
            linha = fonte_pequena.render(f"{i + 1}.  {n}  —  {p} pts", True, cor)
            tela.blit(linha, (LARGURA_TELA // 2 - linha.get_width() // 2, 205 + i * 36))

        rodape = fonte_pequena.render("R = Jogar novamente   |   ESC = Sair", True, (120, 120, 120))
        tela.blit(rodape, (LARGURA_TELA // 2 - rodape.get_width() // 2, 450))

        pygame.display.flip()

def _loop_partida(tela, relogio, fonte_hud, fonte_grande, fonte_pequena, nome_jogador, sons):
    carro_x = LARGURA_TELA // 2 - LARGURA_CARRO // 2
    carro_y = ALTURA_TELA - ALTURA_CARRO - 20

    obs_x, obs_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)
    moeda_cx = LARGURA_TELA // 4
    moeda_cy = -RAIO_MOEDA * 2

    pontos = 0
    vidas = VIDAS_INICIAIS
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_inicio = pygame.time.get_ticks()

    offset_pista = 0.0

    pygame.mixer.stop()

    while True:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.stop()
                return False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.mixer.stop()
                return False

        teclas = pygame.key.get_pressed()
        carro_x = mover_jogador(
            carro_x,
            teclas[pygame.K_LEFT] or teclas[pygame.K_a],
            teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
            VELOCIDADE_CARRO,
            LARGURA_TELA,
            LARGURA_CARRO,
        )
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            carro_y -= VELOCIDADE_CARRO
        
        # Mover para Baixo / Trás (Soma Y)
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            carro_y += VELOCIDADE_CARRO

        # Limitadores para o carro não sair da tela pelas bordas de cima e de baixo
        if carro_y < 0:
            carro_y = 0
        elif carro_y > ALTURA_TELA - ALTURA_CARRO:
            carro_y = ALTURA_TELA - ALTURA_CARRO

        vel = calcular_velocidade(
            VELOCIDADE_OBSTACULO_BASE, pontos, PONTOS_POR_NIVEL, AUMENTO_VELOCIDADE
        )

        obs_y = mover_obstaculo(obs_y, vel)
        moeda_cy = int(mover_obstaculo(moeda_cy, vel * 0.7))
        offset_pista = (offset_pista + vel) % 80

        if obs_y > ALTURA_TELA:
            obs_x, obs_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)
            pontos = calcular_pontos(pontos, 1)

        if moeda_cy - RAIO_MOEDA > ALTURA_TELA:
            mx, moeda_cy = reiniciar_obstaculo(LARGURA_TELA, RAIO_MOEDA * 2)
            moeda_cx = mx + RAIO_MOEDA
            moeda_cy = -RAIO_MOEDA

        carro_rect = pygame.Rect(carro_x, carro_y, LARGURA_CARRO, ALTURA_CARRO)
        obs_rect   = pygame.Rect(obs_x, obs_y, LARGURA_OBSTACULO, ALTURA_OBSTACULO)
        moeda_rect = pygame.Rect(
            moeda_cx - RAIO_MOEDA, moeda_cy - RAIO_MOEDA,
            RAIO_MOEDA * 2, RAIO_MOEDA * 2,
        )

        if verificar_colisao(carro_rect, obs_rect):
            vidas -= 1
            obs_x, obs_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)

        if verificar_colisao(carro_rect, moeda_rect):
            pontos = calcular_pontos(pontos, PONTOS_MOEDA)
            mx, moeda_cy = reiniciar_obstaculo(LARGURA_TELA, RAIO_MOEDA * 2)
            moeda_cx = mx + RAIO_MOEDA
            moeda_cy = -RAIO_MOEDA
            if 'moeda' in sons:
                sons['moeda'].play()

        if pontos > recorde:
            recorde = pontos
            salvar_recorde(CAMINHO_RECORDE, recorde)

        tempo_s = (pygame.time.get_ticks() - tempo_inicio) // 1000

        tela.fill(CINZA)
        _desenhar_pista(tela, offset_pista)
        _desenhar_obstaculo(tela, obs_x, obs_y)
        _desenhar_moeda(tela, moeda_cx, moeda_cy)
        _desenhar_carro(tela, carro_x, carro_y)
        _desenhar_hud(tela, fonte_hud, pontos, recorde, vidas, tempo_s)
        pygame.display.flip()

        if jogador_perdeu(vidas):
            pygame.mixer.stop()
            salvar_ranking(CAMINHO_RANKING, nome_jogador, pontos, TAMANHO_RANKING)
            return _tela_fim(
                tela, relogio, fonte_grande, fonte_hud,
                venceu=False, pontos=pontos, recorde=recorde, nome=nome_jogador,
            )

def executar_jogo():
    pygame.mixer.pre_init(22050, -16, 2, 512)
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte_grande = pygame.font.SysFont(None, 58)
    fonte_hud    = pygame.font.SysFont(None, 30)

    sons = inicializar_som()

    nome_jogador = _tela_nome(tela, relogio, fonte_grande, fonte_hud)
    if nome_jogador is None:
        pygame.quit()
        return

    jogar_novamente = True
    while jogar_novamente:
        jogar_novamente = _loop_partida(
            tela, relogio, fonte_hud, fonte_grande, fonte_hud, nome_jogador, sons
        )

    pygame.quit()