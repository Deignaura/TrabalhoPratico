# Turbo Escape

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Amanda Pimenta
- Bruna Batista
- Clara Lemos
- Deignaura Ribeiro

## Organização planejada

- * **`main.py` / `executar_jogo()`**: Ponto de entrada que gerencia a inicialização e a alternância entre as telas do jogo.
* **`src/config.py`**: Centraliza as constantes do jogo (cores, dimensões da tela, velocidades base, metas e caminhos de arquivos).
* **`src/funcoes.py`**: Contém as regras de física e estados do jogo (`mover_jogador`, `verificar_colisao`, `calcular_velocidade`, `jogador_venceu`, etc).
* **`src/dados.py`**: Responsável pelo sistema de persistência (salvar/carregar recorde máximo e o histórico do ranking local).
* **`data/`**: Pasta que armazena os arquivos de texto (`recorde.txt` e `ranking.txt`).

## Descrição do jogo

O jogador controla um carro em uma estrada 2D com movimentação lateral. Ao iniciar, o jogo solicita o nome do usuário para registro no sistema. Durante a corrida, obstáculos e moedas caem pela pista.

## Objetivo do jogador

Sobreviver aos obstáculos, coletar moedas e atingir a meta de pontos estipulada para vencer e garantir o topo do ranking.

## Regras do jogo
* **Vidas Iniciais:** O jogador começa com 3 vidas.
* **Colisão com Obstáculos:** Cada batida em um obstáculo reduz 1 vida. O obstáculo é reiniciado no topo.
* **Coleta de Moedas:** Cada moeda coletada adiciona uma pontuação bônus (definida em `PONTOS_MOEDA`).
* **Progressão de Dificuldade:** A velocidade da pista e dos elementos aumenta gradualmente com base na pontuação atual do jogador.



## Condição de vitória

O jogador vence o jogo de forma limpa assim que atingir a pontuação máxima definida pela constante `META_PONTOS`.

## Condição de derrota ou encerramento
O jogo exibe a tela de *Game Over* se a quantidade de vidas chegar a 0. Em ambos os finais (vitória ou derrota), o nome e a pontuação são computados no ranking.
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
* **Seta Esquerda / Tecla A**: Mover o carro para a esquerda.
* **Seta Direita / Tecla D**: Mover o carro para a direita.
* **Tecla ENTER**: Confirmar o nome na tela inicial.
* **Tecla R**: Reiniciar uma nova partida na tela de fim de jogo.
* **Tecla ESC**: Sair do jogo a qualquer momento.


## Como executar o projeto

### 1. Clonar o repositório

. Certifique-se de ter o Python 3.x instalado.
2. Clone o repositório e acesse a pasta:
   ```bash
   git clone [https://github.com/Deignaura/TrabalhoPratico.git](https://github.com/Deignaura/TrabalhoPratico.git)
   cd TrabajoPratico

## Como executar os testes

```bash
python -m pytest
```
pip install -r requirements.txt
 ##  Execute  no terminal
python main.py

## Checklist mínimo para entrega
## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
