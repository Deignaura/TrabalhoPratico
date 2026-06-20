import array
import math
import pygame

_FREQ = 22050


def inicializar_som():
    """Gera todos os sons do jogo. Retorna dict vazio se o mixer não estiver disponível."""
    if not pygame.mixer.get_init():
        return {}
    try:
        return {
            'moeda': _criar_moeda(),
            'vitoria': _criar_vitoria(),
        }
    except Exception:
        return {}


def _buf(n_frames):
    return array.array('h', [0] * n_frames * 2)


def _s(val):
    return max(-32767, min(32767, int(val * 32767)))


def _criar_moeda():
    """Ding de duas notas: A5 (880 Hz) seguido de E6 (1320 Hz) com decaimento."""
    n1 = int(_FREQ * 0.10)
    n2 = int(_FREQ * 0.18)
    buf = _buf(n1 + n2)
    for i in range(n1):
        t = i / _FREQ
        v = math.sin(2 * math.pi * 880 * t) * math.exp(-t * 15) * 0.8
        s = _s(v)
        buf[i * 2] = s
        buf[i * 2 + 1] = s
    for i in range(n2):
        t = i / _FREQ
        v = math.sin(2 * math.pi * 1320 * t) * math.exp(-t * 12) * 0.8
        idx = (n1 + i) * 2
        s = _s(v)
        buf[idx] = s
        buf[idx + 1] = s
    return pygame.mixer.Sound(buffer=buf)


def _criar_vitoria():
    """Fanfarra ascendente: C5 → E5 → G5 → C6."""
    notas = [(523, 0.15), (659, 0.15), (784, 0.15), (1047, 0.40)]
    total = sum(int(_FREQ * d) for _, d in notas)
    buf = _buf(total)
    pos = 0
    for freq, dur in notas:
        n = int(_FREQ * dur)
        for i in range(n):
            t = i / _FREQ
            fade = math.exp(-t * 3)
            v = (math.sin(2 * math.pi * freq * t) * 0.7 +
                 math.sin(2 * math.pi * freq * 2 * t) * 0.2) * fade
            idx = (pos + i) * 2
            s = _s(v)
            buf[idx] = s
            buf[idx + 1] = s
        pos += n
    return pygame.mixer.Sound(buffer=buf)
