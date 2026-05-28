# Turbo Escape

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Amanda Pimenta
- Bruna Batista
- Clara Lemos
- Deignaura Ribeiro

## Organização planejada

- `main.py`: inicia o jogo.
-`player.py` controla o carro do jogador
- `assets/`: imagens, fontes e sons.
- `obstacles.py` controla obstaculos.
- `coins.py` controla as moedas.
- `config.py` configurações gerais.
- `utilis.py` funções auxiliadoreas.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

O jogador controlará um carro em uma estrada 2D com movimentação lateral. Durante a corrida, carros, cones e barreiras aparecerão na pista como obstáculos. O objetivo será desviar dos obstáculos enquanto coleta moedas espalhadas pela estrada. Conforme o tempo passa, a velocidade do jogo aumenta, deixando a partida mais difícil e dinâmica.


## Objetivo do jogador

Sobreviver o maior tempo possível, evitar colisões e coletar moedas para alcançar a maior pontuação.

## Regras do jogo

Regra 1: O jogador começa com 3 vidas.
Regra 2: Cada moeda coletada vale 5 pontos.
Regra 3: Cada colisão com obstáculo remove 1 vida.
Regra 4: A velocidade da pista e dos obstáculos aumenta gradualmente.
Regra 5: O jogo termina quando as vidas chegam a zero.


## Condição de vitória

O jogador vence ao atingir determinada pontuação, como 200 pontos, ou sobreviver até o final da corrida.

## Condição de derrota ou encerramento

O jogo termina quando o jogador perde todas as vidas após colidir com obstáculos.
## Elementos previstos no jogo
Jogador ou elemento principal
Descrição:
Um carro controlado pelo teclado que pode se mover para esquerda e direita na pista.
Obstáculos, inimigos ou desafios
Descrição:
Carros, cones e barreiras aparecem aleatoriamente na pista e devem ser evitados.
Itens, alvos ou objetos de interação
Descrição:
Moedas aparecem na estrada e aumentam a pontuação quando coletadas.
Pontuação, vidas, tempo ou progresso
Descrição:
O jogador começa com 3 vidas, coleta moedas para ganhar pontos e enfrenta aumento gradual da velocidade do jogo

## Controles

Seta esquerda / A: mover para esquerda
Seta direita / D: mover para direita
ESC: sair do jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
