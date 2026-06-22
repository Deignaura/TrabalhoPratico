import pygame
import random

from src.config import (
    LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO,
    CINZA, VERMELHO, AZUL, BRANCO, AMARELO, VERDE, PRETO,
    LARGURA_CARRO, ALTURA_CARRO,
    LARGURA_OBSTACULO, ALTURA_OBSTACULO,
    RAIO_MOEDA,
    VELOCIDADE_CARRO, VELOCIDADE_OBSTACULO_BASE,
    AUMENTO_VELOCIDADE, PONTOS_POR_NIVEL, VIDAS_INICIAIS,
    CAMINHO_RECORDE, CAMINHO_RANKING, CAMINHO_RANKING_MOEDAS,TAMANHO_RANKING,
)
from src.funcoes import (
    mover_jogador,
    mover_obstaculo,
    reiniciar_obstaculo,
    verificar_colisao,
    jogador_perdeu,
    jogador_venceu,
    calcular_velocidade,
)
from src.dados import (
    salvar_recorde,
    carregar_recorde,
    salvar_ranking,
    carregar_ranking,
    carregar_moedas,
    salvar_moedas,
    carregar_carro_selecionado,
    salvar_carro_selecionado,
    carregar_carros,
    salvar_carros,
)

cone_img = pygame.image.load("assets/imagens/obstaculos/cone.png")
carro_azul = pygame.image.load("assets/imagens/obstaculos/carro_azul.png")
carro_rosa = pygame.image.load("assets/imagens/obstaculos/carro_rosa.png")
carro_amarelo = pygame.image.load("assets/imagens/obstaculos/carro_amarelo.png")

cone_img = pygame.transform.scale(cone_img, (70, 70))
carro_azul = pygame.transform.scale(carro_azul, (80, 130))
carro_rosa = pygame.transform.scale(carro_rosa, (80, 130))
carro_amarelo = pygame.transform.scale(carro_amarelo, (80, 130))



def _desenhar_carro(tela, x, y):
    """Desenha o carro do jogador na tela com detalhes."""
    carro_atual = carregar_carro_selecionado()

    if carro_atual == "basico":
        tela.blit(carro_basico, (x, y))

    elif carro_atual == "esportivo":
        tela.blit(carro_esportivo, (x, y))

    elif carro_atual == "formula":
        tela.blit(carro_formula, (x, y))


def _desenhar_obstaculo(tela, x, y, tipo):
    """Desenha o obstáculo na tela com detalhes."""
    if tipo == "cone":
        tela.blit(cone_img, (x, y))
    elif tipo == "carro_azul":
        tela.blit(carro_azul, (x, y))
    elif tipo == "carro_rosa":
        tela.blit(carro_rosa, (x, y))
    elif tipo == "carro_amarelo":
        tela.blit(carro_amarelo, (x, y))

def _desenhar_moeda(tela, cx, cy):
    """Desenha a moeda colecionável."""
    tela.blit(
        moeda_img,
        (
            cx - moeda_img.get_width() // 2,
            cy - moeda_img.get_height() // 2,
        ),
    )


def _desenhar_hud(tela, fonte, distancia, recorde, vidas, moedas_partida):
    """Exibe a pontuação, recorde, vidas e tempo na tela."""
    texto = fonte.render(
        f"Distância: {distancia}m  |  Recorde: {recorde}m  |  Moedas: {int(moedas_partida)}  |  Vidas: {vidas}",
        True,
        BRANCO,
    )
    tela.blit(texto, (10, 10))


def _desenhar_pista(tela):
    """Desenha marcações simples de pista no centro."""
    for y in range(0, ALTURA_TELA, 80):
        pygame.draw.rect(tela, (100, 100, 100), (LARGURA_TELA // 2 - 5, y, 10, 40))


# ---------------------------------------------------------------------------
# Telas auxiliares
# ---------------------------------------------------------------------------

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
                    return {
                        "nome": nome.strip(),
                        "acao": "jogar"
                    }
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                elif len(nome) < 15 and evento.unicode.isprintable() and evento.unicode != " " * len(evento.unicode):
                    nome += evento.unicode

        tela.fill(PRETO)

        titulo = fonte_grande.render("TURBO ESCAPE", True, AMARELO)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 130))

        sub = fonte_pequena.render("Desvie dos obstáculos e colete moedas!", True, BRANCO)
        
        moedas = carregar_moedas()
        texto_moedas = fonte_pequena.   render(
            f"Moedas: {moedas}",
            True,
            AMARELO
        )

        tela.blit(sub, (LARGURA_TELA // 2 - sub.get_width() // 2, 210))

        tela.blit(
            texto_moedas,
            (LARGURA_TELA // 2 - texto_moedas.get_width() // 2, 240)
        )

        instrucao = fonte_pequena.render("Digite seu nome e pressione ENTER:", True, (180, 180, 180))
        tela.blit(instrucao, (LARGURA_TELA // 2 - instrucao.get_width() // 2, 290))

        cursor = "_" if (pygame.time.get_ticks() // 500) % 2 == 0 else " "
        caixa = fonte_grande.render(nome + cursor, True, AMARELO)
        tela.blit(caixa, (LARGURA_TELA // 2 - caixa.get_width() // 2, 335))

        dica = fonte_pequena.render("ENTER - Confirmar nome", True, (120, 120, 120))
        tela.blit(dica, (LARGURA_TELA // 2 - dica.get_width() // 2, 430))

        pygame.display.flip()


def _menu_principal(tela, relogio, fonte_grande, fonte_pequena, nome):
    while True:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"

            if evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_RETURN:
                    return "jogar"

                elif evento.key == pygame.K_l:
                    return "loja"
                
                elif evento.key == pygame.K_r:
                    return "ranking"

                elif evento.key == pygame.K_ESCAPE:
                    return "sair"

        tela.fill(PRETO)

        titulo = fonte_grande.render("MENU PRINCIPAL", True, AMARELO)
        tela.blit(
            titulo,
            (LARGURA_TELA // 2 - titulo.get_width() // 2, 80)
        )

        jogador = fonte_pequena.render(
            f"Jogador: {nome}",
            True,
            BRANCO
        )
        tela.blit(
            jogador,
            (LARGURA_TELA // 2 - jogador.get_width() // 320, 170)
        )

        moedas = fonte_pequena.render(
            f"Moedas: {carregar_moedas()}",
            True,
            AMARELO
        )
        tela.blit(
            moedas,
            (LARGURA_TELA // 2 - moedas.get_width() // 320, 210)
        )

        carro_atual = carregar_carro_selecionado()
        carro = fonte_pequena.render(
            f"Carro: {carro_atual.capitalize()}",
            True,
            BRANCO
        )

        tela.blit(
            carro,
            (LARGURA_TELA // 2 - carro.get_width() // 320, 250)
        )

        texto_jogar = fonte_pequena.render("ENTER - Jogar", True, BRANCO)
        texto_loja = fonte_pequena.render("L - Loja", True, BRANCO)
        texto_ranking = fonte_pequena.render("R - Rankings", True, BRANCO)
        texto_sair = fonte_pequena.render("ESC - Sair", True, BRANCO)

        tela.blit(texto_jogar, (LARGURA_TELA // 2 - texto_jogar.get_width() // 320, 330))
        tela.blit(texto_loja, (LARGURA_TELA // 2 - texto_loja.get_width() // 320, 370))
        tela.blit(texto_ranking, (LARGURA_TELA // 2 - texto_ranking.get_width() // 320, 410))
        tela.blit(texto_sair, (LARGURA_TELA // 2 - texto_sair.get_width() // 320, 450))

        carro_atual = carregar_carro_selecionado()

        if carro_atual == "basico":
            imagem = carro_basico
        elif carro_atual == "esportivo":
            imagem = carro_esportivo
        else:
            imagem = carro_formula

        tela.blit(imagem, (200, 250))


        pygame.display.flip()


def _tela_fim(tela, relogio, fonte_grande, fonte_pequena, pontos, recorde, nome):
    """Tela de game over / vitória com ranking. Retorna True para jogar de novo."""
    
    ranking_distancia= carregar_ranking(CAMINHO_RANKING, TAMANHO_RANKING)

    ranking_moedas = carregar_ranking(
        CAMINHO_RANKING_MOEDAS,
        TAMANHO_RANKING
    )

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

        msg = fonte_grande.render("GAME OVER", True, VERMELHO)
        tela.blit(msg, (LARGURA_TELA // 2 - msg.get_width() // 2, 30))

        info = fonte_pequena.render(
            f"Distância: {pontos}m  |   Recorde: {recorde}m", True, BRANCO
        )
        tela.blit(info, (LARGURA_TELA // 2 - info.get_width() // 2, 90))

        titulo1 = fonte_pequena.render("RANKING - DISTÂNCIA", True, AMARELO)
        tela.blit(titulo1, (80, 150))

        for i, (n, p) in enumerate(ranking_distancia):
            cor = AMARELO if n == nome else BRANCO
            linha = fonte_pequena.render(f"{i+1}.  {n}  —  {p} m", True, cor)
            tela.blit(linha, (80, 190 + i * 30))

        titulo2 = fonte_pequena.render("RANKING - MOEDAS",True, AMARELO)
        tela.blit(titulo2, (380, 150))

        for i, (n, m) in enumerate(ranking_moedas):
            cor = AMARELO if n == nome else BRANCO
            linha = fonte_pequena.render(f"{i+1}. {n} - {m}", True, cor)
            tela.blit(linha, (380, 190 + i * 30))

        rodape = fonte_pequena.render("R = Jogar novamente   |   ESC = Sair", True, (120, 120, 120))
        tela.blit(rodape, (LARGURA_TELA // 2 - rodape.get_width() // 2, 450))

        pygame.display.flip()


def _tela_loja(tela, relogio, fonte_grande, fonte_pequena):
    while True:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_1:
                    salvar_carro_selecionado("basico")

                elif evento.key == pygame.K_2:
                    carros = carregar_carros()

                    if "esportivo" not in carros:
                        moedas = carregar_moedas()

                        if moedas >= 50:
                            salvar_moedas(moedas - 50)
                            carros.append("esportivo")
                            salvar_carros(carros)
                            salvar_carro_selecionado("esportivo")
                        else:
                            print("Moedas insuficientes!")
                    else:
                        salvar_carro_selecionado("esportivo")

                elif evento.key == pygame.K_3:
                    carros = carregar_carros()

                    if "formula" not in carros:
                        moedas = carregar_moedas()

                        if moedas >= 100:
                            salvar_moedas(moedas - 100)
                            carros.append("formula")
                            salvar_carros(carros)
                            salvar_carro_selecionado("formula")
                        else:
                            print("Moedas insuficientes!")
                    else:
                        salvar_carro_selecionado("formula")
                
                elif evento.key == pygame.K_ESCAPE:
                    return True

        tela.fill(PRETO)

        carros = carregar_carros()
        carro_atual = carregar_carro_selecionado()

        if carro_atual == "basico":
            status1 = "Selecionado"
        else:
            status1 = "Comprado"


        if carro_atual == "esportivo":
            status2 = "Selecionado"
        elif "esportivo" in carros:
            status2 = "Comprado"
        else:
            status2 = "Bloqueado - $50"


        if carro_atual == "formula":
            status3 = "Selecionado"
        elif "formula" in carros:
            status3 = "Comprado"
        else:
            status3 = "Bloqueado - $100"

        
        nome1 = fonte_pequena.render("1 - Básico", True, BRANCO)
        nome2 = fonte_pequena.render("2 - Esportivo", True, BRANCO)
        nome3 = fonte_pequena.render("3 - Fórmula", True, BRANCO)

        status1_txt = fonte_pequena.render(status1, True, BRANCO)
        status2_txt = fonte_pequena.render(status2, True, BRANCO)
        status3_txt = fonte_pequena.render(status3, True, BRANCO)


        tela.blit(carro_basico, (150, 240))
        tela.blit(carro_esportivo, (360, 240))
        tela.blit(carro_formula, (560, 240))

        tela.blit(nome1, (145, 400))
        tela.blit(nome2, (345, 400))
        tela.blit(nome3, (545, 400))

        tela.blit(status1_txt, (140, 430))
        tela.blit(status2_txt, (335, 430))
        tela.blit(status3_txt, (535, 430))
        
        
        titulo = fonte_grande.render("LOJA", True, AMARELO)
        tela.blit(
            titulo,
            (LARGURA_TELA // 2 - titulo.get_width() // 2, 70)
        )
        
        
        moedas = fonte_pequena.render(
            f"Moedas: {carregar_moedas()}",
            True,
            AMARELO
        )
        tela.blit(
            moedas,
            (LARGURA_TELA // 2 - moedas.get_width() // 2, 150)
        )

        voltar = fonte_pequena.render(
            "ESC - Voltar ao menu", True, BRANCO
        )
        tela.blit(
            voltar,
            (LARGURA_TELA // 2 - voltar.get_width() // 2, 520)
        )

        pygame.display.flip()


def _tela_ranking(tela, relogio, fonte_grande, fonte_pequena):
    ranking_distancia = carregar_ranking(
        CAMINHO_RANKING,
        TAMANHO_RANKING
    )

    ranking_moedas = carregar_ranking(
        CAMINHO_RANKING_MOEDAS,
        TAMANHO_RANKING
    )

    while True:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        tela.fill(PRETO)

        titulo = fonte_grande.render("RANKINGS", True, AMARELO)
        tela.blit(
            titulo,
            (LARGURA_TELA // 2 - titulo.get_width() // 2, 50)
        )

        dist = fonte_pequena.render(
            "Distância",
            True,
            BRANCO
        )
        tela.blit(dist, (170, 200))

        for i, (nome, pontos) in enumerate(ranking_distancia):
            linha = fonte_pequena.render(
                f"{i+1}. {nome} - {pontos} m",
                True,
                BRANCO
            )
            tela.blit(linha, (170, 235 + i * 40))

        moed = fonte_pequena.render(
            "Moedas",
            True,
            AMARELO
        )
        tela.blit(moed, (520, 200))

        for i, (nome, moedas) in enumerate(ranking_moedas):
            linha = fonte_pequena.render(
                f"{i+1}. {nome} - {moedas}",
                True,
                BRANCO
            )
            tela.blit(linha, (520, 235 + i * 40))

        sair = fonte_pequena.render(
            "ESC - Voltar",
            True,
            BRANCO
        )
        tela.blit(
            sair,
            (LARGURA_TELA // 2 - sair.get_width() // 2, 550)
        )

        pygame.display.flip()



# ---------------------------------------------------------------------------
# Loop principal de uma partida
# ---------------------------------------------------------------------------

def _loop_partida(tela, relogio, fonte_hud, fonte_grande, fonte_pequena, nome_jogador):
    """Executa uma partida completa. Retorna True para jogar de novo, False para sair."""
    carro_x = LARGURA_TELA // 2 - LARGURA_CARRO // 2
    carro_y = ALTURA_TELA - ALTURA_CARRO - 20

    obs_x, obs_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)
    tipo_obstaculo = random.choice(["cone", "carro_azul", "carro_rosa", "carro_amarelo"])
    moeda_cx = LARGURA_TELA // 4
    moeda_cy = -RAIO_MOEDA * 2

    distancia = 0
    moedas_partida = 0
    vidas = VIDAS_INICIAIS
    recorde = carregar_recorde(CAMINHO_RECORDE)
    tempo_inicio = pygame.time.get_ticks()

    while True:
        relogio.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return "menu"

        teclas = pygame.key.get_pressed()
        
        carro_atual = carregar_carro_selecionado()
        if carro_atual == "basico":
            velocidade_carro = VELOCIDADE_CARRO * 1.0
        elif carro_atual == "esportivo":
            velocidade_carro = VELOCIDADE_CARRO * 1.2
        else:  
            velocidade_carro = VELOCIDADE_CARRO * 1.5

        if carro_atual == "basico":
            multiplicador_moedas = 1.0
        elif carro_atual == "esportivo":
            multiplicador_moedas = 1.5
        else:  
            multiplicador_moedas = 1.2

        carro_x = mover_jogador(
            carro_x,
            teclas[pygame.K_LEFT] or teclas[pygame.K_a],
            teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
            velocidade_carro,
            LARGURA_TELA,
            LARGURA_CARRO,
        )

        vel = calcular_velocidade(
            VELOCIDADE_OBSTACULO_BASE, distancia, PONTOS_POR_NIVEL, AUMENTO_VELOCIDADE
        )

        obs_y = mover_obstaculo(obs_y, vel)
        moeda_cy = int(mover_obstaculo(moeda_cy, vel * 0.7))

        if obs_y > ALTURA_TELA:
            obs_x, obs_y = reiniciar_obstaculo(LARGURA_TELA, LARGURA_OBSTACULO)
            tipo_obstaculo = random.choice(["cone", "carro_azul", "carro_rosa", "carro_amarelo"])
            distancia += 3

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
            tipo_obstaculo = random.choice(["cone", "carro_azul", "carro_rosa", "carro_amarelo"])

        if verificar_colisao(carro_rect, moeda_rect):
            moedas_partida += multiplicador_moedas
            mx, moeda_cy = reiniciar_obstaculo(LARGURA_TELA, RAIO_MOEDA * 2)
            moeda_cx = mx + RAIO_MOEDA
            moeda_cy = -RAIO_MOEDA

        if distancia > recorde:
            recorde = distancia
            salvar_recorde(CAMINHO_RECORDE, recorde)

        tempo_s = (pygame.time.get_ticks() - tempo_inicio) // 1000

        tela.fill(CINZA)
        _desenhar_pista(tela)
        _desenhar_obstaculo(tela, obs_x, obs_y, tipo_obstaculo)
        _desenhar_moeda(tela, moeda_cx, moeda_cy)
        _desenhar_carro(tela, carro_x, carro_y)
        _desenhar_hud(tela, fonte_hud, distancia, recorde, vidas, moedas_partida)
        pygame.display.flip()

        if jogador_perdeu(vidas):
            moedas_totais = carregar_moedas()
            salvar_moedas (int(moedas_totais + moedas_partida))

            salvar_ranking(CAMINHO_RANKING, nome_jogador, distancia, TAMANHO_RANKING)

            salvar_ranking(CAMINHO_RANKING_MOEDAS, nome_jogador, int(moedas_partida),TAMANHO_RANKING)
            
            return _tela_fim(
                tela, relogio, fonte_grande, fonte_hud, distancia, recorde, nome_jogador,
            )

# ---------------------------------------------------------------------------
# Ponto de entrada
# ---------------------------------------------------------------------------

def executar_jogo():
    """Inicializa o Pygame e gerencia o fluxo geral do jogo."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

    global carro_basico, carro_esportivo, carro_formula

    carro_basico = pygame.image.load(
        "assets/imagens/carros/basico.png"
    ).convert_alpha()
    carro_basico = pygame.transform.scale(carro_basico, (80, 140))

    carro_esportivo = pygame.image.load(
        "assets/imagens/carros/esportivo.png"
    ).convert_alpha()
    carro_esportivo = pygame.transform.scale(carro_esportivo, (80, 140))

    carro_formula = pygame.image.load(
        "assets/imagens/carros/formula.png"
    ).convert_alpha()
    carro_formula = pygame.transform.scale(carro_formula, (80, 140))

    global moeda_img

    moeda_img = pygame.image.load(
        "assets/imagens/moeda/moeda.png"
    ).convert_alpha()

    moeda_img = pygame.transform.scale(moeda_img, (45, 45))

    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()
    fonte_grande = pygame.font.SysFont(None, 58)
    fonte_hud    = pygame.font.SysFont(None, 30)

    resultado =  _tela_nome(tela, relogio, fonte_grande, fonte_hud)
    if resultado is None:
        pygame.quit()
        return
    nome_jogador = resultado["nome"]

    while True:
        acao = _menu_principal(
            tela,
            relogio,
            fonte_grande,
            fonte_hud,
            nome_jogador
        )

        if acao == "jogar":
            resultado_partida = _loop_partida(
                tela,
                relogio,
                fonte_hud,
                fonte_grande,
                fonte_hud,
                nome_jogador
            )
            if resultado_partida == "menu":
                continue

        elif acao == "loja":
            _tela_loja(
                tela,
                relogio,
                fonte_grande,
                fonte_hud
            )

        elif acao == "ranking":
            _tela_ranking(
                tela,
                relogio,
                fonte_grande,
                fonte_hud
            )

        elif acao == "sair":
            break

    pygame.quit()
