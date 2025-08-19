# main.py

from modelo_grafo import mapa, criar_grafo
from algoritmos import dijkstra, pagerank, bellman_ford # Apenas Dijkstra é suficiente para o exemplo
from plotagem import plotar_grafo
import networkx as nx

def exibir_menu_principal():
    """
    Exibe o menu principal para o usuário, valida a entrada e retorna a opção escolhida.

    Returns:
        int: O número da opção escolhida pelo usuário (1 a 4).
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
                return escolha_int # Retorna a escolha válida e sai da função
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

    # Usaremos Dijkstra
    caminho, custo = dijkstra(mapa, origem, destino)

    if caminho:
        print(f"\nCaminho mais curto: {' -> '.join(caminho)}")
        print(f"Duração total: {custo} minutos")
        if mostrar_grafo:
            plotar_grafo(G, pos, caminho=caminho, titulo=f"Rota Mais Rápida: de {origem} para {destino}")
        print('\n' + '/'*50)
    else:
        print(f"Não foi possível encontrar um caminho de {origem} para {destino}.")

def analisar_pagerank(G, pos):
    """
    Função placeholder para a análise de PageRank.
    """
    print("\n--- Análise de Importância (PageRank) ---")
    print("Esta funcionalidade ainda não foi implementada.")
    # Aqui, no futuro, chamaríamos a função de cálculo do PageRank
    # e uma função de visualização apropriada.
    pass # 'pass' é uma instrução que não faz nada, usada como placeholder.


def main():
    """
    Função principal que executa o programa e gerencia o menu.
    """
    # O grafo é criado apenas uma vez, no início.

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
            analisar_pagerank(G, None)

        elif escolha == 4:
            print("\nObrigado por usar o sistema. Até logo!")
            break # Quebra o loop while e encerra o programa



# Ponto de entrada do programa
if __name__ == "__main__":
    main()