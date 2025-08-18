import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

def formatar_tempo(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    if horas > 0:
        return f"{horas}h {minutos_restantes}min"
    else:
        return f"{minutos_restantes}min"

graph = {
    'Bela Vista': {'Uepa': 5, 'Cidade Nova': 6},
    'Uepa': {'FL33': 7, 'Bambuzal': 5, 'Bela Vista': 5, 'Cidade Nova': 4},
    'FL33': {'Uepa': 7, 'C1': 6, 'C2': 10, 'C3': 16, 'Bambuzal': 6, 'Verdes Mares': 4, 'São Félix': 19, 'Cidade Nova': 9, 'Shopping': 5},
    'C1': {'C3': 13, 'C2': 6, 'São Félix': 15, 'Verdes Mares': 3, 'FL33': 6, 'Shopping': 6},
    'C2': {'FL33': 10, 'C1': 6, 'São Félix': 10, 'Verdes Mares': 7, 'Transmangueira': 10},
    'Bambuzal': {'FL33': 6, 'Uepa': 10, 'Verdes Mares': 4, 'Transmangueira': 4},
    'Transmangueira': {'Verdes Mares': 9, 'C2': 11, 'Bambuzal': 8},
    'Verdes Mares': {'FL33': 4, 'C2': 9, 'Transmangueira': 9, 'Bambuzal': 6, 'C1': 3},
    'C3': {'C2': 17, 'C1': 13, 'FL33': 16, 'Cidade Jardim': 10},
    'São Félix': {'C1': 15, 'C2': 10, 'Verdes Mares': 17, 'FL33': 19, 'Morada Nova': 15},
    'Morada Nova': {'São Félix': 15},
    'Cidade Jardim': {'C3': 10, 'Shopping': 7},
    'Shopping': {'Cidade Jardim': 7, 'C1': 6, 'FL33': 5},
    'Cidade Nova': {'Bela Vista': 6, 'Uepa': 4, 'FL33': 9}
}

def plot_grafo(graph):
    G = nx.DiGraph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue",
            font_size=10, font_weight="bold", arrows=True, arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
    plt.title("Grafo com seus respectivos pesos")
    plt.show()
    plt.tight_layout()

def bellman_ford(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    predecessor = {node: None for node in graph}
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    predecessor[neighbor] = node
    for node in graph:
        for neighbor, weight in graph[node].items():
            if dist[node] + weight < dist[neighbor]:
                raise ValueError("Grafo contém ciclo de peso negativo")
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessor[current_node]
    return dist[end], path

def rota_todos_os_pontos(graph, start):
    todos_os_pontos = list(graph.keys())
    caminho_total = []
    tempo_total = 0
    ponto_atual = start
    todos_os_pontos.remove(ponto_atual)
    caminho_total.append(ponto_atual)
    while todos_os_pontos:
        menor_custo = float('inf')
        proximo_ponto = None
        melhor_caminho = []
        for ponto in todos_os_pontos:
            custo, caminho = bellman_ford(graph, ponto_atual, ponto)
            if custo < menor_custo:
                menor_custo = custo
                proximo_ponto = ponto
                melhor_caminho = caminho
        if menor_custo == float('inf'):
            return float('inf'), []
        for ponto in melhor_caminho[1:]:
            if ponto not in caminho_total:
                caminho_total.append(ponto)
        tempo_total += menor_custo
        ponto_atual = proximo_ponto
        todos_os_pontos.remove(proximo_ponto)
    return tempo_total, caminho_total

def calcular_pagerank(graph):
    G = nx.DiGraph()
    for node, edges in graph.items():
        for neighbor, weight in edges.items():
            G.add_edge(node, neighbor, weight=weight)
    pr = nx.pagerank(G, weight='weight')
    return pr

def remover_bloqueios(graph, bloqueios_afetados):
    new_graph = deepcopy(graph)
    for node1, node2 in bloqueios_afetados:
        if node1 in new_graph and node2 in new_graph[node1]:
            del new_graph[node1][node2]
        if node2 in new_graph and node1 in new_graph[node2]:
            del new_graph[node2][node1]
    return new_graph

start_node = 'Morada Nova'
tempo_total, rota_completa = rota_todos_os_pontos(graph, start_node)
print("BELLMAN-FORD\n")
print(f"Rota completa original passando por todos os pontos, começando em {start_node}:\n")
print("O ônibus passará pelos seguintes pontos:")
for ponto in rota_completa:
    print(f"- {ponto}")
print(f"\nO tempo total estimado de viagem é: {formatar_tempo(tempo_total)}.")

page_rank = calcular_pagerank(graph)
print("\n** PageRank dos nós **:")
for node, rank in sorted(page_rank.items(), key=lambda x: x[1], reverse=True):
    print(f"{node}: {rank:.4f}")

bloqueios_afetados = [('FI33', 'C2'), ('Uepa', 'Bambuzal')]
print(f"\n\n*** Manifestação detectada nos bloqueios {bloqueios_afetados}. Recalculando a rota... ***\n")
graph_modificado = remover_bloqueios(graph, bloqueios_afetados)
tempo_total_alterado, rota_completa_alterada = rota_todos_os_pontos(graph_modificado, start_node)
print(f"\nDevido à manifestação, o trajeto será alterado:\n")
print("O ônibus passará pelos seguintes pontos:")
if tempo_total_alterado == float('inf'):
    print("Não há rota possível devido à manifestação.")
else:
    for ponto in rota_completa_alterada:
        print(f"- {ponto}")
if tempo_total_alterado == float('inf'):
    print(f"\nO tempo total estimado de viagem após a alteração é: Inviável.")
else:
    print(f"\nO tempo total estimado de viagem após a alteração é: {formatar_tempo(tempo_total_alterado)}.")
print("\n** Explicação da mudança de rota devido à manifestação **:")
print("Devido às manifestações, algumas vias que costumavam estar abertas agora estão bloqueadas.")
print("Com o bloqueio dessas vias, o trajeto teve que ser replanejado.")
print("O ônibus agora precisa seguir por novos caminhos para chegar aos pontos finais.")
print("Isso pode ter aumentado o tempo de viagem ou até mesmo deixado a rota impossível, se não houver alternativas.")
plot_grafo(graph)

def bloquear_ponto(graph, ponto):
    novo_grafo = deepcopy(graph)
    if ponto in novo_grafo:
        del novo_grafo[ponto]
    for node in novo_grafo:
        if ponto in novo_grafo[node]:
            del novo_grafo[node][ponto]
    return novo_grafo

def calcular_menor_rota_sem_ponto_bloqueado(graph, ponto_bloqueado, ponto_inicial, ponto_final):
    graph_modificado = bloquear_ponto(graph, ponto_bloqueado)
    try:
        tempo_viagem, caminho_rota = bellman_ford(graph_modificado, ponto_inicial, ponto_final)
        return tempo_viagem, caminho_rota
    except ValueError as e:
        return str(e), []

def interagir_com_usuario_e_calcular_rota_sem_bloqueio(graph):
    bloquear = input("Você deseja bloquear algum ponto no grafo? (sim/não): ").strip().lower()
    ponto_bloqueado = None
    if bloquear == "sim":
        ponto_bloqueado = input("Digite o nome do ponto que deseja bloquear: ").strip()
    ponto_inicial = input("Digite o ponto de partida: ").strip()
    ponto_final = input("Digite o ponto de chegada: ").strip()
    if ponto_bloqueado:
        tempo_viagem, caminho_rota = calcular_menor_rota_sem_ponto_bloqueado(graph, ponto_bloqueado, ponto_inicial, ponto_final)
        if tempo_viagem == "Grafo contém ciclo de peso negativo":
            print(f"\nErro: {tempo_viagem}.")
        elif tempo_viagem == float('inf'):
            print(f"\nNão é possível chegar de {ponto_inicial} a {ponto_final} sem passar por {ponto_bloqueado}.")
        else:
            print(f"\nO tempo estimado de viagem de {ponto_inicial} a {ponto_final}, sem passar por {ponto_bloqueado}, é: {formatar_tempo(tempo_viagem)}.")
            print(f"O caminho percorrido será: {' -> '.join(caminho_rota)}")
    else:
        tempo_viagem, caminho_rota = bellman_ford(graph, ponto_inicial, ponto_final)
        if tempo_viagem == "Grafo contém ciclo de peso negativo":
            print(f"\nErro: {tempo_viagem}.")
        elif tempo_viagem == float('inf'):
            print(f"\nNão é possível chegar de {ponto_inicial} a {ponto_final}.")
        else:
            print(f"\nO tempo estimado de viagem de {ponto_inicial} a {ponto_final} é: {formatar_tempo(tempo_viagem)}.")
            print(f"O caminho percorrido será: {' -> '.join(caminho_rota)}")
    input("\nPressione Enter duas vezes para encerrar.")
    input()

interagir_com_usuario_e_calcular_rota_sem_bloqueio(graph)
