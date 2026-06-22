# Testes

Esta pasta contém testes automatizados do projeto.

## Arquivos

- `test_logica.py`: valida funções puras de lógica em `src/funcoes.py`.

## Como executar

```bash
python -m pytest
```

## Funções cobertas pelos testes

| Função | O que é verificado |
|---|---|
| `mover_jogador` | Movimento horizontal dentro e fora dos limites da tela |
| `mover_jogador_vertical` | Movimento vertical dentro dos limites `y_min` e `y_max` |
| `verificar_colisao` | Detecção de sobreposição entre retângulos |
| `calcular_velocidade` | Aumento progressivo de velocidade por nível |
| `jogador_perdeu` | Condição de derrota ao zerar as vidas |

## Boas práticas

- Crie testes para toda regra de pontuação, vidas e condições de fim de jogo.
- Prefira funções pequenas e testáveis no módulo `src/funcoes.py`.
