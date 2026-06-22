# Código-fonte (`src`)

Esta pasta contém os módulos principais do jogo.

## Arquivos

- `jogo.py`: loop principal, telas (nome, menu, loja, ranking, fim de jogo) e renderização.
- `config.py`: constantes globais (tela, cores, velocidades, caminhos, FPS).
- `funcoes.py`: funções auxiliares de regra e lógica do jogo.
- `dados.py`: leitura e gravação de dados (recorde, ranking de distância, ranking de moedas e total de moedas).
- `sons.py`: geração programática dos efeitos sonoros via síntese de onda.
- `sprites.py`: carregamento e recorte de spritesheet.

## Funções em `funcoes.py`

| Função | Descrição |
|---|---|
| `mover_jogador` | Move o carro horizontalmente (eixo X) dentro dos limites da tela |
| `mover_jogador_vertical` | Move o carro verticalmente (eixo Y) dentro dos limites definidos |
| `mover_obstaculo` | Desloca um elemento para baixo na tela |
| `reiniciar_obstaculo` | Gera nova posição aleatória acima da tela para um elemento |
| `verificar_colisao` | Detecta sobreposição entre dois retângulos do Pygame |
| `calcular_velocidade` | Calcula velocidade dos obstáculos com base na distância percorrida |
| `jogador_perdeu` | Retorna `True` quando o jogador não tem mais vidas |
| `jogador_venceu` | Retorna `True` quando o jogador atinge a meta de pontos |

## Telas em `jogo.py`

| Tela | Função | Descrição |
|---|---|---|
| Nome | `_tela_nome` | Captura o nome do jogador antes do menu |
| Menu principal | `_menu_principal` | Navega para jogar, loja, ranking ou sair |
| Partida | `_loop_partida` | Loop principal do jogo com física, colisões e renderização |
| Loja | `_tela_loja` | Compra e seleção de carros com moedas acumuladas |
| Ranking | `_tela_ranking` | Exibe top 5 por distância e top 5 por moedas |
| Fim de jogo | `_tela_fim` | Game over com rankings e opção de reiniciar |
