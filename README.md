# Objetivos 
O objetivo do projeto foi adotar novas tecnologias para melhorar a eficiência do sistema de transporte público de Marabá (PA). Um dos desafios principais foi otimizar as rotas dos ônibus para garantir que os cidadãos possam se deslocar de maneira eficiente entre diferentes pontos da cidade, aproveitando o máximo de suas rotas, minimizando o tempo de deslocamento e o custo operacional. Entre os objetivos específicos destacam-se:

## 📌 Encontrar as rotas mais eficientes
Utilizar o Algoritmo de Dijkstra e o Algoritmo de Bellman-Ford para determinar as rotas mais curtas entre os principais núcleos da cidade (Cidade Jardim, Nova Marabá, Cidade Nova, Marabá Pioneira, São Félix e Morada Nova).

## 📌 Analisar a importância dos pontos de interesse
Aplicar o Algoritmo de PageRank para ponderar os pontos de interesse dentro da rede de transporte, ou seja, definir os pontos mais importantes/mais críticos na rede, pelos quais a maior parte das rotas passam.

## 📌 Simulação e otimização
Considerar um cenário onde uma rota importante é temporariamente interrompida e utilizar os algoritmos mencionados para redirecionar as rotas e minimizar o impacto sobre os usuários do transporte.

# Metodologia e desenvolvimento 
Para atingir o resultado desejado foi modelado o sistema de transporte público como um grafo, onde os pontos de ônibus são representados como vértices e as rotas possíveis entre eles como arestas, com pesos que refletem o tempo de viagem ou a distância.

## Modelagem do grafo

## Escolha do algoritmo
