![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

# Índice
- [Objetivos](#objetivos)
- [Metodologia e desenvolvimento](#metodologia-e-desenvolvimento)
- [Comparação dos Algoritmos](#comparação-dos-algoritmos)
- [Conclusão](#conclusão)

# Objetivos 
O objetivo do projeto foi adotar novas tecnologias para melhorar a eficiência do sistema de transporte público de Marabá (PA). Um dos desafios principais foi otimizar as rotas dos ônibus para garantir que os cidadãos possam se deslocar de maneira eficiente entre diferentes pontos da cidade, aproveitando o máximo de suas rotas, minimizando o tempo de deslocamento e o custo operacional. Entre os objetivos específicos destacam-se:

### 📌 Encontrar as rotas mais eficientes
Utilizar o Algoritmo de Dijkstra e o Algoritmo de Bellman-Ford para determinar as rotas mais curtas entre os principais núcleos da cidade (Cidade Jardim, Nova Marabá, Cidade Nova, Marabá Pioneira, São Félix e Morada Nova).

### 📌 Analisar a importância dos pontos de interesse
Aplicar o Algoritmo de PageRank para ponderar os pontos de interesse dentro da rede de transporte, ou seja, definir os pontos mais importantes/mais críticos na rede, pelos quais a maior parte das rotas passam.

### 📌 Simulação e otimização
Considerar um cenário onde uma rota importante é temporariamente interrompida e utilizar os algoritmos mencionados para redirecionar as rotas e minimizar o impacto sobre os usuários do transporte.

# Metodologia e desenvolvimento 
Para atingir o resultado desejado foi modelado o sistema de transporte público como um grafo, onde os pontos de ônibus são representados como vértices e as rotas possíveis entre eles como arestas, com pesos que refletem o tempo de viagem ou a distância.

### Modelagem do grafo
O grafo apresentado foi construído com base no mapa urbano da região de Marabá-PA, considerando pontos estratégicos que representam bairros e polos educacionais importantes. Nele, destacam-se localidades como Morada Nova, São Félix, os três campi da Unifesspa (C1, C2 e C3), as folhas 26 e 33 da Nova Marabá, além de áreas centrais como a Transmangueira, Bambuzal, UEPA e a Avenida Bela Vista. As conexões entre os nós simbolizam rotas de deslocamento entre esses pontos, com pesos representando distâncias ou tempos estimados de trajeto, o que permite a aplicação de algoritmos de otimização para melhorar o transporte público local.

![Grafo Gerado](Dijkstra/grafo_transporte_maraba.png)

### ♦️ Algoritmo ([Dijkstra](Dijkstra/main.py))
O algoritmo de Dijkstra é utilizado para determinar o trajeto mais curto em grafos cujas arestas possuem pesos positivos ou nulos. Por isso, ele é bastante eficiente em aplicações como sistemas de transporte, onde tempo e distância não podem ser negativos. Além disso, ele se destaca pelo bom desempenho ao lidar com grafos de grande porte e com muitas conexões.

### ♦️ Algoritmo ([Bellman-Ford](Bellmanford/main.py))
O algoritmo de Bellman-Ford se destaca por aceitar arestas com pesos negativos, o que o torna útil em cenários onde há penalidades de custo, como em horários de pico ou quando é preciso considerar rotas alternativas.

# Comparação dos Algoritmos
Tanto Dijkstra quanto Bellman-Ford têm o objetivo de achar o caminho mais curto dentro de uma rede (ou grafo, no linguajar da computação). Mas cada um tem suas particularidades, vantagens e limitações dependendo do cenário.

O algoritmo de Dijkstra é o queridinho quando os dados do sistema (como tempo de viagem, distância ou custo) são todos positivos. Isso significa que ele funciona super bem em situações simples, onde não existem descontos, penalidades ou integrações tarifárias. Por isso, é bastante usado em aplicativos como Google Maps e Waze, que priorizam velocidade e eficiência. Contudo, *ele não consegue lidar com valores negativos*. Nesse tipo de cenário, quem brilha é o Bellman-Ford, uma vez que ele é mais flexível e aceita pesos negativos. Além disso, ele consegue detectar ciclos negativos, como casos de falhas no sistema tarifário. O ponto fraco do Bellman-Ford é que *ele é mais lento*, principalmente em redes grandes. Isso pode ser um problema em aplicativos que precisam responder rápido.

Se olharmos para o lado da programação, a diferença também é clara. O Dijkstra é mais rápido e performático, mas exige um cuidado maior na hora de programar e não pode ser
usado com pesos negativos. Já o Bellman-Ford é mais simples de implementar (basta ir ajustando os valores das rotas várias vezes), mas pode demorar mais para rodar devido sua maior complexidade. O benefício é que ele é mais seguro em situações complexas, e ainda consegue detectar erros lógicos na estrutura da rede.

**No caso do trabalho proposto**, o algoritmo de Dijkstra se sobressaiu, uma vez que priorizamos velocidade. Além disso, os dados envolvidos são todos positivos e diretos, não implementamos ao sistema políticas públicas, integrações tarifárias ou análise de falhas, por isso o uso do Bellman-Ford (que é mais complexo e lento) foi dispensado.

# Conclusão
Este trabalho realizou uma comparação entre os algoritmos Dijkstra e Bellman-Ford aplicados à melhoria das rotas em um sistema de transporte público. Ambos os métodos mostraram-se eficazes ao resolver o desafio de identificar o caminho mais curto em grafos. Cada um se destacou por características próprias: 

- 🏆 Dijkstra teve desempenho rápido em situações com pesos sempre positivos;
- 🏆 Bellman-Ford demonstrou maior flexibilidade ao lidar com situações que envolvem penalidades, como engarrafamentos.

No entanto, na prática, os dois forneceram resultados muito parecidos, tanto nas rotas encontradas quanto no tempo estimado dos trajetos. Além disso, ao aplicar restrições de percurso, observou-se que ambos os algoritmos foram capazes de recalcular os caminhos com eficiência, garantindo que o serviço continuasse operando mesmo diante de bloqueios. Em vista disso, tanto Dijkstra quanto Bellman-Ford se mostraram adequados para a otimização de rotas em sistemas de mobilidade. A escolha entre eles dependerá do contexto e das características específicas do problema a ser resolvido, sendo ambos ferramentas úteis.
