import networkx as nx
from copy import deepcopy
import matplotlib.pyplot as plt

def plotar_grafo(G, pos, caminho=None, titulo=""):
    """
    Desenha um grafo na tela usando matplotlib, com setas corrigidas.
    """
    plt.figure(figsize=(12, 8))
    
    # --- Adicionado: Variável para consistência ---
    tamanho_no = 1500  # Defina o tamanho do nó aqui

    # Desenha os nós e seus rótulos
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=tamanho_no)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    
    labels_arestas = nx.get_edge_attributes(G, 'weight')

    if caminho:
        
        arestas_caminho = list(zip(caminho, caminho[1:]))
        outras_arestas = []
        for aresta in G.edges():
            if aresta not in arestas_caminho:
                aresta_reciproca = (aresta[1], aresta[0])
                if aresta_reciproca in arestas_caminho or aresta in arestas_caminho:
                    continue
                else:
                    outras_arestas.append(aresta)

        nx.draw_networkx_edges(
            G, pos,
            edgelist=outras_arestas,
            edge_color='gray',
            arrows=True,
            arrowsize=20,
            node_size=tamanho_no
        )
        
        nx.draw_networkx_edges(
            G, pos,
            edgelist=arestas_caminho,
            edge_color='green',
            width=2.5,
            arrows=True,
            arrowsize=25,
            node_size=1470
        )
        
        nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color='lightgreen', node_size=tamanho_no)
        
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_arestas, font_size=9)

    else:
        nx.draw_networkx_edges(
            G, pos,
            arrows=True,
            arrowsize=20,
            edge_color="#574F5F",
            node_size=tamanho_no
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_arestas, font_size=9)

    plt.title(titulo, fontweight="bold", fontsize="x-large")
    plt.tight_layout()
    plt.show()
