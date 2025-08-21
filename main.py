# main.py

from modelo_grafo import mapa, criar_grafo
from algoritmos import dijkstra, pagerank
from plotagem import plotar_grafo, plotar_grafo_pagerank
import networkx as nx

def exibir_menu_principal():
    """
    Returns: número da opção escolhida pelo usuário (1 a 4).
    """
    
    while True:
        print("\nPor favor, escolha uma das opções abaixo:\n")
        print("1. Visualizar o mapa completo da rede")
        print("2. Simular a rota mais curta entre dois pontos")
        print("3. Analisar a importância dos pontos (PageRank)")
        print("4. Sair do programa\n")

        escolha = input("Digite o número da sua opção: ")

        if escolha.isdigit():
            escolha_int = int(escolha)
            if 1 <= escolha_int <= 4:
                return escolha_int 
            else:
                print("\n[ERRO] Opção inválida. Por favor, escolha um número entre 1 e 4.")
        else:
            print("\n[ERRO] Entrada inválida. Por favor, digite apenas o número da opção.")

def iniciar_simulacao_rota(G, pos):
    """
    Coordena a simulação de rota, pedindo origem e destino ao usuário.
    """
    
    print('\n' + '/'*50)
    print("\n-------- Simulação de Rota Mais Curta --------")

    nos_disponiveis = list(G.nodes)

    print(f"\nPontos disponíveis: {', '.join(nos_disponiveis)}")
    print("-"*76)
    print("Digite 'ocultar' a qualquer momento para desativar/ativar exibição do grafo.")
    print("-"*76 + "\n")
    
    mostrar_grafo = True

    while True:
        origem = input("Digite o ponto de partida (ou 'voltar' para o menu): ")
        if origem == 'voltar': return
        if origem == 'ocultar':
            if mostrar_grafo:
                mostrar_grafo = False
                print("--- !! Visualização OFF !! ---")
            else:
                mostrar_grafo = True
                print("--- Visualização ON ---")
            continue
        if origem in nos_disponiveis:
            break
        print("[ERRO] Ponto de partida inválido. Tente novamente.")

    while True:
        destino = input("Digite o ponto de destino (ou 'voltar' para o menu): ")
        if destino == 'voltar': return
        if destino == 'ocultar':
            if mostrar_grafo:
                mostrar_grafo = False
                print("--- !! Visualização OFF !! ---")
            else:
                mostrar_grafo = True
                print("--- Visualização ON ---")
            continue
        if destino in nos_disponiveis:
            break
        print("[ERRO] Ponto de destino inválido. Tente novamente.")

    # O algortimo utilizado foi o Dijkstra, para entender o motivo da escolhe consulte a sessão 'Comparação de Algoritmos' no README.md
    caminho, custo = dijkstra(mapa, origem, destino)

    if caminho:
        print(f"\nCaminho mais curto: {' -> '.join(caminho)}")
        print(f"Duração total: {custo} minutos")
        if mostrar_grafo:
            plotar_grafo(G, pos, caminho=caminho, titulo=f"Rota Mais Rápida: de {origem} para {destino}")
        print('\n' + '/'*50)
    else:
        print(f"Não foi possível encontrar um caminho de {origem} para {destino}.")

# MELHORIA: Função para analisar a importância dos pontos usando PageRank

def analisar_pagerank(G, pos):
    """
    Calcula o PageRank para o grafo e exibe o resultado visualmente.
    """
    print("\n--- Análise de Importância (PageRank) ---")
    print("Calculando a importância de cada ponto na rede...")

    pagerank_scores = pagerank(mapa)

    pontos_ordenados = sorted(pagerank_scores.items(), key=lambda item: item[1], reverse=True)
    
    print("\nPontos mais importantes da rede (maior score primeiro):")
    for i, (ponto, score) in enumerate(pontos_ordenados):
        print(f"{i+1}. {ponto}: {score:.4f}")

    plotar_grafo_pagerank(
        G, 
        pos, 
        pagerank_scores, 
        "Visualização da Importância dos Pontos (PageRank)"
    )
    print('\n' + '/'*50)


def main():
    """
    Função principal que executa o programa e gerencia o menu.
    """

    G = criar_grafo(mapa)

    pos = nx.spring_layout(G, seed=23)
    
    print("\n" + "="*50)
    print("   Sistema de Otimização de Rotas de Transporte   ")
    print("="*50)

    while True:
        escolha = exibir_menu_principal()

        if escolha == 1:
            print("\nExibindo o mapa completo da rede...")
            plotar_grafo(G, pos, None, "Mapa Completo da Rede de Transporte")
        
        elif escolha == 2:
            iniciar_simulacao_rota(G, pos)

        elif escolha == 3:
            analisar_pagerank(G, pos)

        elif escolha == 4:
            print("\nObrigado por usar o sistema. Até logo!")
            break

if __name__ == "__main__":
    main()