def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo == "":
                return 0
            return int(conteudo)
    except FileNotFoundError:
        return 0


def carregar_ranking(caminho_arquivo, tamanho=5):
    """Retorna lista de (nome, pontos) ordenada do maior para o menor."""
    ranking = []
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if ":" in linha:
                    partes = linha.split(":", 1)
                    nome = partes[0]
                    try:
                        pts = int(partes[1])
                        ranking.append((nome, pts))
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass
    ranking.sort(key=lambda item: item[1], reverse=True)
    return ranking[:tamanho]


def salvar_ranking(caminho_arquivo, nome, pontos, tamanho=5):
    """Insere nova entrada no ranking e persiste os top N."""
    nome_limpo = nome.replace(":", "").replace("\n", "").strip()
    ranking = carregar_ranking(caminho_arquivo, tamanho * 2)
    ranking.append((nome_limpo, pontos))
    ranking.sort(key=lambda item: item[1], reverse=True)
    ranking = ranking[:tamanho]
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for n, p in ranking:
            arquivo.write(f"{n}:{p}\n")
