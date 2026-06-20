# Turbo Escape

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Amanda Pimenta
- Bruna Batista
- Clara Lemos
- Deignaura Ribeiro

---

## Descrição do jogo

O jogador controla um carro vermelho em uma estrada 2D vista de cima. A estrada rola para baixo continuamente, dando a sensação de movimento. Obstáculos e moedas aparecem na pista: o jogador deve desviar dos obstáculos e coletar o máximo de moedas possível. A velocidade aumenta progressivamente, tornando o jogo cada vez mais difícil. Não há condição de vitória — o objetivo é bater o próprio recorde.

## Objetivo do jogador

Coletar o maior número de moedas possível antes de perder todas as vidas. A pontuação máxima é salva automaticamente entre sessões.

---

## Regras

| Regra | Detalhe |
|---|---|
| Vidas iniciais | 3 vidas |
| Colisão com obstáculo | Perde 1 vida; obstáculo é reiniciado no topo |
| Coleta de moeda | +5 pontos; efeito sonoro reproduzido |
| Passagem de obstáculo | +1 ponto |
| Progressão de dificuldade | Velocidade aumenta a cada 10 pontos |
| Fim de jogo | Ao perder as 3 vidas |

## Condição de derrota

O jogo termina e exibe a tela de **Game Over** quando o jogador perde todas as 3 vidas ao colidir com obstáculos. A pontuação é registrada no ranking.

---

## Controles

| Tecla | Ação |
|---|---|
| Seta Esquerda / A | Mover para a esquerda |
| Seta Direita / D | Mover para a direita |
| Seta Cima / W | Mover para frente |
| Seta Baixo / S | Mover para trás |
| ENTER | Confirmar nome na tela inicial |
| R | Reiniciar partida na tela de fim de jogo |
| ESC | Sair do jogo |

---

## Organização do código

```
TrabalhoPratico/
├── main.py              # Ponto de entrada
├── src/
│   ├── jogo.py          # Loop principal, eventos, renderização
│   ├── config.py        # Constantes globais (tela, cores, velocidades)
│   ├── funcoes.py       # Regras de física e lógica do jogo
│   ├── dados.py         # Leitura e gravação de recorde e ranking
│   ├── sons.py          # Geração programática dos efeitos sonoros
│   └── sprites.py       # Carregamento de spritesheet
├── assets/
│   ├── imagens/         # Sprites e imagens
│   ├── fontes/          # Fontes personalizadas
│   └── sons/            # Pasta reservada para arquivos de áudio externos
├── data/
│   ├── recorde.txt      # Pontuação máxima salva
│   └── ranking.txt      # Top 5 melhores partidas
├── docs/
│   └── proposta.MD      # Proposta inicial do projeto
└── tests/
    └── test_logica.py   # Testes unitários com pytest
```

---

## Como executar

### Pré-requisitos

- Python 3.10+
- Pygame

### Instalação

```bash
git clone https://github.com/Deignaura/TrabalhoPratico.git
cd TrabalhoPratico
pip install -r requirements.txt
```

### Executar o jogo

```bash
python main.py
```

### Executar os testes

```bash
python -m pytest
```

---

## Sons

Os efeitos sonoros são gerados programaticamente em Python puro (módulo `array` + síntese de onda), sem necessidade de arquivos externos:

- **Coleta de moeda**: dois tons encadeados (A5 → E6) com decaimento exponencial.

Se o dispositivo não tiver placa de som disponível, o jogo continua normalmente sem áudio.
