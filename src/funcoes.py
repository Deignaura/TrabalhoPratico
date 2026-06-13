import random


def mover_jogador(x, esquerda, direita, velocidade, largura_tela, largura_carro):
    """Move o carro horizontalmente dentro dos limites da tela."""
    if esquerda and x > 0:
        x -= velocidade
    if direita and x < largura_tela - largura_carro:
        x += velocidade
    return x


def mover_obstaculo(y, velocidade):
<<<<<<< HEAD
    """Desce o obstáculo na tela."""
    return y + velocidade


def reiniciar_obstaculo(largura_tela, largura_obstaculo):
    """Retorna nova posição (x, y) aleatória acima da tela para o obstáculo."""
    x = random.randint(0, largura_tela - largura_obstaculo)
    y = -largura_obstaculo
=======
    """Desce um elemento na tela."""
    return y + velocidade


def reiniciar_obstaculo(largura_tela, largura_elemento):
    """Retorna nova posição (x, y) aleatória acima da tela para um elemento."""
    x = random.randint(0, largura_tela - largura_elemento)
    y = -largura_elemento
>>>>>>> 784f53c8a5a5dc843d3f44f4a620fe2c074ef9be
    return x, y


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


<<<<<<< HEAD
def calcular_pontos(pontos):
    """Incrementa a pontuação em 1 ponto."""
    return pontos + 1
=======
def calcular_pontos(pontos, ganhos=1):
    """Incrementa a pontuação com o valor ganho."""
    return pontos + ganhos
>>>>>>> 784f53c8a5a5dc843d3f44f4a620fe2c074ef9be


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0
<<<<<<< HEAD
=======


def jogador_venceu(pontos, meta):
    """Indica se o jogador atingiu a pontuação meta."""
    return pontos >= meta


def calcular_velocidade(base, pontos, pontos_por_nivel, aumento):
    """Aumenta a velocidade a cada bloco de pontos completado."""
    nivel = pontos // pontos_por_nivel
    return base + nivel * aumento


def limitar_valor(valor, minimo, maximo):
    """Restringe um valor ao intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor
>>>>>>> 784f53c8a5a5dc843d3f44f4a620fe2c074ef9be
