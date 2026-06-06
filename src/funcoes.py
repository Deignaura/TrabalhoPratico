import random


def mover_jogador(x, esquerda, direita, velocidade, largura_tela, largura_carro):
    """Move o carro horizontalmente dentro dos limites da tela."""
    if esquerda and x > 0:
        x -= velocidade
    if direita and x < largura_tela - largura_carro:
        x += velocidade
    return x


def mover_obstaculo(y, velocidade):
    """Desce o obstáculo na tela."""
    return y + velocidade


def reiniciar_obstaculo(largura_tela, largura_obstaculo):
    """Retorna nova posição (x, y) aleatória acima da tela para o obstáculo."""
    x = random.randint(0, largura_tela - largura_obstaculo)
    y = -largura_obstaculo
    return x, y


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def calcular_pontos(pontos):
    """Incrementa a pontuação em 1 ponto."""
    return pontos + 1


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0
