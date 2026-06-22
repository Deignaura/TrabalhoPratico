# Turbo Escape

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

- Amanda Pimenta
- Bruna Batista
- Clara Lemos
- Deignaura Ribeiro

---

## Descrição do jogo

O jogador controla um carro em uma estrada 2D vista de cima. As faixas centrais da pista rolam continuamente para baixo, dando sensação de movimento. Obstáculos (cones e carros adversários) e moedas aparecem na pista: o jogador deve desviar dos obstáculos e coletar o máximo de moedas possível. A velocidade aumenta progressivamente, tornando o jogo cada vez mais difícil. Não há condição de vitória — o objetivo é bater o próprio recorde.

O jogo conta com uma **loja** onde moedas coletadas podem ser usadas para desbloquear novos carros, cada um com velocidade e multiplicador de moedas distintos.

## Objetivo do jogador

Percorrer a maior distância possível e coletar o máximo de moedas antes de perder todas as vidas. Distância e moedas são registradas em rankings separados, salvos automaticamente entre sessões.

---

## Regras

| Regra | Detalhe |
|---|---|
| Vidas iniciais | 3 vidas |
| Colisão com obstáculo | Perde 1 vida; obstáculo é reiniciado no topo |
| Coleta de moeda | +1 moeda (×1.5 com Esportivo, ×1.2 com Fórmula); efeito sonoro reproduzido |
| Passagem de obstáculo | +3 metros de distância |
| Progressão de dificuldade | Velocidade dos obstáculos aumenta a cada 10 metros |
| Fim de jogo | Ao perder as 3 vidas |

## Obstáculos

| Obstáculo | Tipo |
|---|---|
| Cone laranja | Cone de sinalização |
| Carro azul | Carro adversário |
| Carro rosa | Carro adversário |
| Carro amarelo | Carro adversário |

## Carros disponíveis

| Carro | Custo | Velocidade | Multiplicador de moedas |
|---|---|---|---|
| Básico | Grátis | Normal (×1.0) | ×1.0 |
| Esportivo | 50 moedas | Rápido (×1.2) | ×1.5 |
| Fórmula | 100 moedas | Muito rápido (×1.5) | ×1.2 |

## Condição de derrota

O jogo termina e exibe a tela de **Game Over** quando o jogador perde todas as 3 vidas ao colidir com obstáculos. Distância percorrida e moedas coletadas na partida são registradas nos rankings.

---

## Controles

### Tela inicial / Menu principal

| Tecla | Ação |
|---|---|
| ENTER | Confirmar nome / Iniciar partida |
| L | Abrir loja |
| R | Ver rankings |
| ESC | Sair do jogo |

### Durante a partida

| Tecla | Ação |
|---|---|
| Seta Esquerda / A | Mover o carro para a esquerda |
| Seta Direita / D | Mover o carro para a direita |
| Seta Cima / W | Mover o carro para frente (sobe na pista) |
| Seta Baixo / S | Mover o carro para trás (desce na pista) |
| ESC | Pausar e voltar ao menu principal |

### Tela de fim de jogo

| Tecla | Ação |
|---|---|
| R | Jogar novamente |
| ESC | Voltar ao menu principal |

---

## Organização do código

```
TrabalhoPratico/
├── main.py                  # Ponto de entrada
├── src/
│   ├── jogo.py              # Loop principal, telas, eventos, renderização
│   ├── config.py            # Constantes globais (tela, cores, velocidades, caminhos)
│   ├── funcoes.py           # Regras de física e lógica do jogo
│   ├── dados.py             # Leitura e gravação de recorde, ranking e moedas
│   ├── sons.py              # Geração programática dos efeitos sonoros
│   └── sprites.py           # Carregamento de spritesheet
├── assets/
│   ├── imagens/
│   │   ├── carros/          # basico.png, esportivo.png, formula.png
│   │   ├── moeda/           # moeda.png
│   │   └── obstaculos/      # cone.png, carro_azul.png, carro_rosa.png, carro_amarelo.png
│   ├── fontes/              # Fontes tipográficas personalizadas
│   └── sons/                # Pasta reservada para arquivos de áudio externos
├── data/
│   ├── recorde.txt          # Melhor distância registrada
│   ├── ranking.txt          # Top 5 por distância percorrida
│   ├── ranking_moedas.txt   # Top 5 por moedas coletadas
│   └── moedas.txt           # Total de moedas acumuladas pelo jogador
├── docs/
│   └── proposta.MD          # Proposta inicial do projeto
└── tests/
    └── test_logica.py       # Testes unitários com pytest
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

| Evento | Descrição do som |
|---|---|
| Coleta de moeda | Dois tons encadeados (A5 → E6) com decaimento exponencial |

O mixer é pré-inicializado antes do Pygame (`pygame.mixer.pre_init`) para garantir compatibilidade. Se o dispositivo não tiver placa de som disponível, o jogo continua normalmente sem áudio.
