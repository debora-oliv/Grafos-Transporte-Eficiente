import heapq
import networkx as nx
from copy import deepcopy
import matplotlib.pyplot as plt

mapa = {
    'Bela Vista': {'Uepa': 5},
    'Uepa': {'FL33': 7, 'Bambuzal': 5, 'Bela Vista': 5},
    'FL33': {'Uepa': 7, 'C1': 6, 'C2': 10, 'C3': 16, 'Bambuzal': 6, 'FL26': 4, 'São Félix': 19},
    'C1': {'C3': 13, 'C2': 6, 'São Félix': 15, 'FL26': 3, 'FL33': 6},
    'C2': {'FL33': 10, 'C1': 6, 'São Félix': 10, 'FL26': 7, 'Transmangueira': 10},
    'Bambuzal': {'FL33': 6, 'Uepa': 10, 'FL26': 4, 'Transmangueira': 4},
    'Transmangueira': {'FL26': 9, 'C2': 11, 'Bambuzal': 8},
    'FL26': {'FL33': 4, 'C2': 9, 'Transmangueira': 9, 'Bambuzal': 6, 'C1': 3},
    'C3': {'C2': 17, 'C1': 13, 'FL33': 16},
    'São Félix': {'C1': 15, 'C2': 10, 'FL26': 17, 'FL33': 19, 'Morada Nova': 15},
    'Morada Nova': {'São Félix': 15}
}

def dijkstra(grafo, inicio, fim):
    fila = [(0, inicio, [])]
    visitados = set()
    while fila:
        custo, atual, percurso = heapq.heappop(fila)
        if atual in visitados:
            continue
        percurso = percurso + [atual]
        if atual == fim:
            return custo, percurso
        visitados.add(atual)
        for vizinho, peso in grafo[atual].items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, percurso))
    return float("inf"), []

def rota_total(grafo):
    origem = 'Transmangueira'
    destino = 'C2'
    restantes = list(grafo.keys())
    rota = [origem]
    total = 0
    atual = origem
    restantes.remove(origem)

    while restantes:
        menor = float('inf')
        proximo = None
        trecho = []
        for ponto in restantes:
            custo, trajeto = dijkstra(grafo, atual, ponto)
            if custo < menor:
                menor = custo
                proximo = ponto
                trecho = trajeto
        for local in trecho[1:]:
            if local not in rota:
                rota.append(local)
        total += menor
        atual = proximo
        restantes.remove(proximo)
    return total, rota

def pagerank(grafo):
    G = nx.DiGraph()
    for origem, destinos in grafo.items():
        for destino, peso in destinos.items():
            G.add_edge(origem, destino, weight=peso)
    return nx.pagerank(G, weight='weight')

def tempo_formatado(mins):
    h = mins // 60
    m = mins % 60
    return f"{h} horas e {m} minutos" if h else f"{m} minutos"

def rota_entre_pontos(grafo, inicio, fim):
    tempo, trajeto = dijkstra(grafo, inicio, fim)
    print(f"\nTrajeto entre {inicio} e {fim}:")
    for local in trajeto:
        print(f"- {local}")
    print(f"Tempo estimado: {tempo_formatado(tempo)}")

    ranking = pagerank(grafo)
    print("\nImportância dos pontos (PageRank):")
    for ponto, valor in sorted(ranking.items(), key=lambda x: x[1], reverse=True):
        print(f"- {ponto}: importância {valor:.4f}")

def rota_com_bloqueio(grafo, caminho, bloqueios):
    novo = deepcopy(grafo)
    for a, b in bloqueios:
        novo[a].pop(b, None)
        novo[b].pop(a, None)

    nova_rota = []
    total = 0
    for i in range(len(caminho) - 1):
        a, b = caminho[i], caminho[i+1]
        custo, trajeto = dijkstra(novo, a, b)
        if custo == float('inf'):
            print(f"Bloqueio entre {a} e {b}, sem rota alternativa.")
            return None, None
        nova_rota.extend(trajeto[1:])
        total += custo
    return total, nova_rota

def remover_ponto(grafo):
    if input("\nDeseja bloquear um ponto? (sim/não): ").lower() != 'sim':
        print("Nenhum bloqueio feito.")
        return

    bloqueado = input("Nome do ponto a bloquear: ")
    if bloqueado not in grafo:
        print(f"Ponto {bloqueado} inexistente.")
        return

    modificado = deepcopy(grafo)
    modificado.pop(bloqueado)
    for conexoes in modificado.values():
        conexoes.pop(bloqueado, None)

    origem = input("Ponto de entrada: ")
    destino = input("Ponto de destino: ")
    tempo, trajeto = dijkstra(modificado, origem, destino)

    if trajeto:
        print(f"\nNovo caminho de {origem} a {destino} sem {bloqueado}:")
        for p in trajeto:
            print(f"- {p}")
        print(f"Tempo: {tempo_formatado(tempo)}")
    else:
        print("Não foi possível encontrar rota alternativa.")

def plotar_grafo(grafo):
    G = nx.DiGraph()
    for origem, destinos in grafo.items():
        for destino, peso in destinos.items():
            G.add_edge(origem, destino, weight=peso)

    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500,
            font_size=10, font_weight='bold', arrows=True, arrowsize=20)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=9)
    plt.title("Visualização do Grafo de Conexões")
    plt.tight_layout()
    plt.show()

def executar():
    print("== Caminho completo de Transmangueira até C2 ==")

    plotar_grafo(mapa)

    tempo, trajeto = rota_total(mapa)

    print("\nRota planejada:")
    for local in trajeto:
        print(f"- {local}")
    print(f"Tempo total: {tempo_formatado(tempo)}")

    entrada = input("\nDigite o ponto inicial: ")
    saida = input("Digite o ponto final: ")
    rota_entre_pontos(mapa, entrada, saida)

    remover_ponto(mapa)

executar()
