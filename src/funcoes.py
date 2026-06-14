import random

def mover_jogador(x, esquerda, direita, velocidade, largura_tela, largura_carro):
    if esquerda and x > 0:
        x -= velocidade
    if direita and x < largura_tela - largura_carro:
        x += velocidade
    return x


def mover_obstaculo(y, velocidade):
    return y + velocidade


def reiniciar_obstaculo(largura_tela, largura_elemento):
    x = random.randint(0, largura_tela - largura_elemento)
    y = -largura_elemento
    return x, y


def verificar_colisao(retangulo_1, retangulo_2):
    return retangulo_1.colliderect(retangulo_2)


def calcular_pontos(pontos, ganhos=1):
    return pontos + ganhos


def jogador_perdeu(vidas):
    return vidas <= 0


def jogador_venceu(pontos, meta):
    return pontos >= meta


def calcular_velocidade(base, pontos, pontos_por_nivel, aumento):
    nivel = pontos // pontos_por_nivel
    return base + nivel * aumento


def limitar_valor(valor, minimo, maximo):
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor