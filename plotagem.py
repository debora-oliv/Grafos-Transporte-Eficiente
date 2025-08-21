import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm

def plotar_grafo(G, pos, caminho=None, titulo=""):
    """
    Args:
        G (nx.DiGraph): grafo a ser desenhado.
        pos (dict): dicionário com as posições dos nós.
        caminho (list, optional): lista de nós representando o caminho a ser destacado.
        titulo (str, optional): título do gráfico.
    """
    plt.figure(figsize=(14, 9))
    
    estilo_base_nos = {"node_size": 2000, "node_color": "skyblue"}
    estilo_base_arestas = {"edge_color": "#574F5F", "arrowsize": 20, "width": 1.0}
    estilo_base_rotulos = {"font_size": 10, "font_weight": "bold"}
    
    # Grafo principal sem caminho definido
    nx.draw_networkx_nodes(G, pos, **estilo_base_nos)
    nx.draw_networkx_edges(G, pos, **estilo_base_arestas)
    nx.draw_networkx_labels(G, pos, **estilo_base_rotulos)
    
    labels_arestas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_arestas, font_size=9)

    # Se um caminho for definido, desenha o destaque por cima do grafo base
    if caminho:
        estilo_caminho_nos = {"node_size": 2200, "node_color": "lightgreen"}
        estilo_caminho_arestas = {"edge_color": "green", "width": 2.5, "arrowsize": 25}
        
        arestas_caminho = list(zip(caminho, caminho[1:]))
        
        nx.draw_networkx_edges(G, pos, edgelist=arestas_caminho, **estilo_caminho_arestas)
        
        nx.draw_networkx_nodes(G, pos, nodelist=caminho, **estilo_caminho_nos)
        
        # MELHORIA: destaque especial para origem e destino
        origem, destino = caminho[0], caminho[-1]
        
        nx.draw_networkx_nodes(G, pos, nodelist=[origem], node_size=2300, node_color="#00FF00")

        nx.draw_networkx_nodes(G, pos, nodelist=[destino], node_size=2300, node_color="#FF4500")

        nx.draw_networkx_labels(G, pos, **estilo_base_rotulos)

    plt.title(titulo, fontweight="bold", fontsize="x-large")
    plt.tight_layout()
    plt.margins(0.05)
    plt.show()

 # MELHORIA: Função para plotar o grafo com PageRank
def plotar_grafo_pagerank(G, pos, pagerank_scores, titulo=""):
    plt.figure(figsize=(14, 9))

    nos = list(pagerank_scores.keys())
    scores = list(pagerank_scores.values())

    # --- Lógica para o tamanho dos nós ---
    min_size = 1500
    max_size = 6000
    tamanhos_nos = [min_size + (score - min(scores)) / (max(scores) - min(scores)) * (max_size - min_size) for score in scores]

    # --- Lógica para a cor dos nós ---
    cmap = cm.get_cmap('viridis') # Outras opções: 'plasma', 'inferno', 'magma', 'cividis'
    norm = colors.Normalize(vmin=min(scores), vmax=max(scores))
    cores_nos = cmap(norm(scores))

    nx.draw_networkx_nodes(G, pos, nodelist=nos, node_size=tamanhos_nos, node_color=cores_nos)
    nx.draw_networkx_edges(G, pos, edge_color="gray", arrowsize=15, alpha=0.7)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", font_color="black")
    
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, shrink=0.8)
    cbar.set_label('Importância (PageRank Score)', weight='bold')

    plt.title(titulo, fontweight="bold", fontsize="x-large")
    plt.tight_layout()
    plt.margins(0.05)
    plt.show()