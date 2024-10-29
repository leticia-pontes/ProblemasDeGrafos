import timeit

def mostrar_grafo(grafo):
    print("\nGrafo:")
    for vertice, adjacentes in grafo.items():
        print(f"{vertice}: ", end="")
        for adjacente, peso in adjacentes:
            print(f"{vertice}-{adjacente} ({peso}) ->", end=" ")
        print("null")

def bellman_ford(grafo, inicio):
    # pega o número de vértices do grafo
    v = len(grafo)

    # define as distâncias como infinitas
    distancias = {vertice: float("inf") for vertice in grafo}

    # define a distância do vértice inicial (ponto de partida) como 0, já que se trata de um laço
    distancias[inicio] = 0

    # cria uma lista de arestas a partir do grafo
    arestas = []
    for u in grafo:
        for v, peso in grafo[u]:
            arestas.append((u, v, peso))

    # relaxa todas as arestas (V - 1) vezes
    for _ in range(v - 1):
        for u, v, peso in arestas:
            if distancias[u] != float("inf") and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso

    # verifica a existência de ciclos negativos
    for u, v, peso in arestas:
        if distancias[u] != float("inf") and distancias[u] + peso < distancias[v]:
            print("\nO grafo contém um ciclo de peso negativo")
            print("Não é possível determinar distâncias válidas.\n")
            return
    """
    As distâncias não podem ser confiáveis em casos de ciclos negativos
    """

    # exibe as distâncias mais curtas do vértice inicial para cada vértice
    print(f"\nDistâncias a partir do vértice {inicio}\n")
    for vertice in grafo:
        print(f"{vertice}: {'inf' if distancias[vertice] == float('inf') else distancias[vertice]}")
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
    # bellman_ford(grafo, inicio)

    tempo = timeit.timeit(lambda: bellman_ford(grafo, inicio), number=1000)
    print(f"\nTempo médio de execução do algoritmo de Bellman-Ford (1000 execuções): {tempo:.6f} segundos\n")

if __name__ == '__main__':
    main()
