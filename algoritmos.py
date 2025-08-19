import heapq
import networkx as nx
from copy import deepcopy

def dijkstra(grafo, inicio, fim):
    fila = [(0, inicio, [])]
    visitados = set()
    while fila:
        custo, atual, percurso = heapq.heappop(fila)
        if atual in visitados:
            continue
        percurso = percurso + [atual]
        if atual == fim:
            return percurso, custo
        visitados.add(atual)
        for vizinho, peso in grafo[atual].items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, percurso))
    return [], float("inf")

def bellman_ford(graph, start, end):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    antecessor = {node: None for node in graph}
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    antecessor[neighbor] = node
    for node in graph:
        for neighbor, weight in graph[node].items():
            if dist[node] + weight < dist[neighbor]:
                raise ValueError("Grafo contém ciclo de peso negativo")
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = antecessor[current_node]
    return dist[end], path

def pagerank(grafo):
    G = nx.DiGraph()
    for origem, destinos in grafo.items():
        for destino, peso in destinos.items():
            G.add_edge(origem, destino, weight=peso)
    return nx.pagerank(G, weight='weight')