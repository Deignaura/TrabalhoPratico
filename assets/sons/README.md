# Sons

Pasta reservada para arquivos de áudio externos (`.wav`, `.ogg`, `.mp3`).

## Estado atual

Os efeitos sonoros do jogo são gerados programaticamente em `src/sons.py` usando síntese de onda com o módulo `array` do Python, sem necessidade de arquivos nesta pasta.

## Sons implementados

| Identificador | Evento de disparo | Descrição técnica |
|---|---|---|
| `moeda` | Coleta de moeda durante a partida | Dois tons encadeados: A5 (880 Hz) seguido de E6 (1320 Hz), com decaimento exponencial |
| `vitoria` | Reservado para uso futuro | Fanfarra ascendente: C5 → E5 → G5 → C6 |

## Inicialização

O mixer é pré-inicializado com `pygame.mixer.pre_init(22050, -16, 2, 512)` antes do `pygame.init()`. Se o dispositivo não suportar áudio, `inicializar_som()` retorna um dicionário vazio e o jogo continua sem som.

## Caso queira adicionar arquivos externos

- Prefira `.ogg` para músicas e `.wav` para efeitos curtos.
- Normalize o volume para evitar diferenças bruscas entre arquivos.
- Documente a origem dos áudios quando forem de terceiros.
