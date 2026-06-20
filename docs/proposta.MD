# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Turbo Escape

Exemplo:

> Corrida dos Obstáculos

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Amanda Pimenta 
- Nome 2: Bruna Batista
- Nome 3: Clara Lemos
- Nome 4: Deignaura Ribeiro

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

Jogo de desviar de obstáculos;

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

O jogador controlará um carro em uma estrada 2D com movimentação lateral. Durante a corrida, carros, cones e barreiras aparecerão na pista como obstáculos. O objetivo será desviar dos obstáculos enquanto coleta moedas espalhadas pela estrada. Conforme o tempo passa, a velocidade do jogo aumenta, deixando a partida mais difícil e dinâmica.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

Sobreviver o maior tempo possível, evitar colisões e coletar moedas para alcançar a maior pontuação.

## 6. Regras principais

Liste as principais regras do jogo.

Regras do grupo:

- Regra 1:  O jogador começa com 3 vidas.
- Regra 2:  Cada moeda coletada vale 5 pontos.
- Regra 3:  Cada colisão com obstáculo remove
- Regra 4:  A velocidade da pista e dos obstáculos aumenta gradualmente.
- Regra 5:  O jogo termina quando as vidas chegam a zero.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

Não há condição de vitória fixa. O jogo é baseado em recorde: o objetivo é coletar o maior número de moedas possível antes de perder todas as vidas. A pontuação máxima é salva automaticamente entre sessões.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

O jogo termina quando o jogador perde todas as vidas após colidir com obstáculos.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

 Um carro controlado pelo teclado que pode se mover para esquerda, direita, frente e para trás na pista.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

Carros aparecem aleatoriamente na pista e devem ser evitados. 

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

Moedas aparecem na estrada e aumentam a pontuação quando coletadas. 

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

 O jogador começa com 3 vidas, coleta moedas para ganhar pontos e enfrenta aumento gradual da velocidade do jogo

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando:Seta esquerda / A: mover para esquerda 
- Tecla/comando: Seta direita / D: mover para direita 
- Tecla/comando: Seta cima / W: mover para cima
- Tecla/comando: Seta baixo / S: mover para baixo
- Tecla/comando: R: para tentar de novo
- Tecla/comando: ESC: sair do jogo

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

- `main.py`: ponto de entrada — chama `executar_jogo()`.
- `src/jogo.py`: loop principal, eventos, atualização e renderização.
- `src/config.py`: constantes globais (tela, cores, velocidades, caminhos).
- `src/funcoes.py`: funções auxiliares de regra e lógica.
- `src/dados.py`: leitura e gravação de recorde e ranking.
- `src/sons.py`: geração programática dos efeitos sonoros.
- `src/sprites.py`: carregamento e recorte de spritesheet.
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (`recorde.txt` e `ranking.txt`).
- `tests/`: testes unitários com pytest.
- `docs/`: documentação do projeto, incluindo esta proposta.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

Os sons do jogo (coleta de moeda) são gerados programaticamente com Python puro, sem arquivos externos, usando síntese de onda via módulo `array`. Os gráficos são desenhados com as primitivas do Pygame. Não foram utilizados recursos externos de terceiros.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Implementação das colisões entre jogador, obstáculos e moedas.
- Dificuldade 2: Controle do aumento gradual da velocidade do jogo.
- Dificuldade 3: Organização do código em módulos e realização de testes com pytest.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

A versão mínima do jogo terá um carro controlado pelo teclado, obstáculos aparecendo na pista, sistema de vidas, coleta de moedas, pontuação, aumento de dificuldade e tela de fim de jogo.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias implementadas:

- Tela inicial com captura de nome do jogador.
- Sistema de ranking e recorde persistido em arquivo.
- Efeito de estrada rolando para simular movimento real do carro.
- Efeito sonoro ao coletar moeda (síntese programática).
- Aumento gradual de dificuldade conforme a pontuação cresce.