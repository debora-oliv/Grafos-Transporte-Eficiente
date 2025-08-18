import networkx as nx
from copy import deepcopy
import matplotlib.pyplot as plt

mapa = {
    'Bela Vista': {'Uepa': 5, 'Cidade Nova': 6},
    'Uepa': {'FL33': 7, 'Bambuzal': 5, 'Bela Vista': 5, 'Cidade Nova': 4},
    'FL33': {'Uepa': 7, 'C1': 6, 'C2': 10, 'Bambuzal': 6, 'Verdes Mares': 4, 'São Félix': 19, 'Cidade Nova': 9, 'Shopping': 5, 'Cidade Jardim':10},
    'C1': {'C2': 6, 'São Félix': 15, 'Verdes Mares': 3, 'FL33': 6, 'Shopping': 6},
    'C2': {'FL33': 10, 'C1': 6, 'São Félix': 10, 'Verdes Mares': 7, 'Transmangueira': 10},
    'Bambuzal': {'FL33': 6, 'Uepa': 10, 'Verdes Mares': 4, 'Transmangueira': 4},
    'Transmangueira': {'Verdes Mares': 9, 'C2': 11, 'Bambuzal': 8},
    'Verdes Mares': {'FL33': 4, 'C2': 9, 'Transmangueira': 9, 'Bambuzal': 6, 'C1': 3},
    'C3': {'Cidade Jardim': 10},
    'São Félix': {'C1': 15, 'C2': 10, 'Verdes Mares': 17, 'FL33': 19, 'Morada Nova': 15},
    'Morada Nova': {'São Félix': 15},
    'Cidade Jardim': {'C3': 10, 'Shopping': 7, 'FL33':10},
    'Shopping': {'Cidade Jardim': 7, 'C1': 6, 'FL33': 5},
    'Cidade Nova': {'Bela Vista': 6, 'Uepa': 4, 'FL33': 9}
}

def criar_grafo(dict):
    """
    Cria e retorna um objeto de grafo do NetworkX a partir de um dicionário.
    Esta função cuida apenas da estrutura de dados.
    """
    G = nx.DiGraph()
    for origem, destinos in dict.items():
        for destino, peso in destinos.items():
            G.add_edge(origem, destino, weight=peso)
    return G