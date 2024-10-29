# biblioteca para fila/pilha
import heapq
import timeit

def mostrar_grafo(grafo):
    print("\nGrafo:")
    for vertice, adjacentes in grafo.items():
        print(f"{vertice}: ", end="")
        for adjacente, peso in adjacentes:
            print(f"{vertice}-{adjacente} ({peso}) ->", end=" ")
        print("null")

def dijkstra(grafo, inicio):
    # pega o número de vértices do grafo
    v = len(grafo)

    """
    Essa variável será atualizada no decorrer da função e retornada no final.
    A lista 'distancias' mantém a menor distância conhecida de cada vértice ao vértice inicial.
    Inicialmente, todas as distâncias são definidas como infinitas (ou seja, inatingíveis), exceto para o vértice inicial, que é 0.
    """
    
    # define as distâncias como infinitas
    distancias = [float("inf")] * v

    # define a distância do vértice inicial (ponto de partida) como 0, já que se trata de um laço
    distancias[inicio] = 0

    # inicia uma fila de prioridade
    fila_prioridade = [(0, inicio)]  # (distancia, vértice)

    # enquanto houver vértices para serem processados na fila de prioridade
    while fila_prioridade:

        # retorna o vértice com a menor distância
        distancia_atual, u = heapq.heappop(fila_prioridade)

        # se a distância atual for maior que a registrada, ignore (essa distância já não é válida)
        if distancia_atual > distancias[u]:
            continue

        # pega cada um dos vértices adjacentes a u (vértice atual)
        for vizinho, peso in grafo[u]:
            # define a nova distância
            nova_distancia = distancia_atual + peso

            """
            Se a nova distância calculada for menor do que a distância atualmente conhecida para o vértice vizinho, atualiza a distância.
            """
            if nova_distancia < distancias[vizinho]:
                # atualiza a distância com o valor menor
                distancias[vizinho] = nova_distancia

                # adiciona o vizinho e a nova distância à fila de prioridade
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
                """
                Fila de prioridade garante que o próximo vértice a ser processado será sempre aquele com a menor distância conhecida.
                """

    print("\nDistâncias mais curtas a partir do vértice inicial\n")
    for i, distancia in enumerate(distancias):
        print(f"{i}: {'inf' if distancia == float('inf') else distancia}")
    print()

def main():

    """
    Grafo com pesos positivos
    """
    grafo = {
        0: [(1, 5), (2, 7), (6, 4)],
        1: [(3, 6), (4, 3)],
        2: [(0, 5), (5, 8), (6, 2)],
        3: [(0, 7), (7, 9)],
        4: [(1, 6), (6, 5), (8, 3)],
        5: [(1, 3), (5, 4), (7, 1)],
        6: [(2, 8), (4, 4), (8, 6)],
        7: [(0, 4), (2, 2), (5, 5)],
        8: [(3, 9), (5, 1), (8, 7)],
        9: [(4, 3), (6, 6), (8, 7)]
    }

    """
    O algoritmo de Dijkstra não consegue encontrar a menor distância se o grafo possuir pesos negativos,
    porque ele assume que, uma vez que um vértice é marcado como visitado, sua menor distância é conhecida. 
    Como essa suposição não é verdadeira com arestas negativas, o algoritmo não encontra a menor distância corretamente.
    """
    
    """
    Grafo com pesos negativos (sem ciclos negativos)
    """
    # grafo = {
    #     0: [(1, 4), (2, -1)],
    #     1: [(3, 2)],
    #     2: [(3, 5), (4, 2)],
    #     3: [(5, 1)],
    #     4: [(5, -2)],
    #     5: [(6, 3)],
    #     6: [(7, 4)],
    #     7: [(8, 1)],
    #     8: [(9, 2)],
    #     9: []
    # }

    """
    Grafo com ciclos negativos
        Ciclo 1: 0 → 1 → 3 → 0
        Ciclo 2: 2 → 0 → 1 → 2
        Ciclo 3: 2 → 6 → 4 → 1 → 3 → 0 → 2
        Ciclo 4: 6 → 4 → 1 → 3 → 0 → 2 → 6
    """
    # grafo = {
    #     0: [(1, -5), (2, -7), (6, -4)],
    #     1: [(3, -6), (4, -3)],
    #     2: [(0, -5), (5, -8), (6, -2)],
    #     3: [(0, -7), (7, -9)],
    #     4: [(1, -6), (6, -5), (8, -3)],
    #     5: [(1, -3), (5, -4), (7, -1)],
    #     6: [(2, -8), (4, -4), (8, -6)],
    #     7: [(0, -4), (2, -2), (5, -5)],
    #     8: [(3, -9), (5, -1), (8, -7)],
    #     9: [(4, -3), (6, -6), (8, -7)]
    # }

    mostrar_grafo(grafo)

    inicio = int(input("\nDigite o vértice inicial: "))    
    # dijkstra(grafo, inicio)

    tempo = timeit.timeit(lambda: dijkstra(grafo, inicio), number=1000)
    print(f"\nTempo médio de execução do algoritmo de Dijkstra (1000 execuções): {tempo:.6f} segundos\n")

if __name__ == "__main__":
    main()
