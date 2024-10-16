# biblioteca para fila/pilha
import heapq

def mostrar_grafo(grafo):
    print()
    for i, adjacentes in enumerate(grafo):
        vertice = i + 1
        print(f"* Vértice {vertice}: ", end="")
        for adjacente, peso in adjacentes:
            print(f"{vertice}-{adjacente} ({peso}) ->", end=" ")
        print("null")
        print()

def dijkstra(grafo, inicio, aresta_excluida):

    # pega o número de vértices do grafo
    v = len(grafo)

    """
    sssa variável será atualizada no decorrer da função e retornada no final.
    a lista 'distancias' mantém a menor distância conhecida de cada vértice 
    ao vértice inicial.
    inicialmente, todas as distâncias são definidas como 
    infinitas (ou seja, inatingíveis) exceto para o vértice inicial que é 0.
    """

    # define as distâncias como infinitas
    distancias = [float("inf")] * v

    # define a distância do vértice inicial (ponto de partida) como 0, já que se trata de um laço
    distancias[inicio] = 0

    # inicia uma fila de prioridade
    fila_prioridade = [(0, inicio)] # (distancia, vértice)

    # enquanto houver vértices para serem processados na fila de prioridade
    while fila_prioridade:

        # retorna o vértice com a menor distância
        distancia_atual, u = heapq.heappop(fila_prioridade)

        # se a distância atual for maior que a registrada, ignore (essa distância já não é válida)
        if distancia_atual > distancias[u]:
            continue

        # pega cada um dos vértices adjacentes a u (vértice atual)
        for vizinho, peso in grafo[u]:

            # ignora a aresta especificada
            if (u + 1, vizinho) == aresta_excluida or (vizinho, u + 1) == aresta_excluida:
                continue

            # define a nova distância
            nova_distancia = distancia_atual + peso

            """
            se a nova distância calculada for menor do que a distância atualmente 
            conhecida para o vértice vizinho, atualiza a distância.
            """
            if nova_distancia < distancias[vizinho - 1]:

                # atualiza a distância com o valor menor
                distancias[vizinho - 1] = nova_distancia

                # adiciona o vizinho e a nova distância à fila de prioridade
                # a fila de prioridade garante que o próximo vértice a ser processado será sempre aquele com a menor distância conhecida.
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho - 1))

    # retorna a lista com as distâncias mais curtas
    return distancias

def main():
    # vértices e arestas
    v, e = map(int, input("\nVértices e arestas: ").split())

    # inicializa o grafo com listas de adjacência
    grafo = [[] for _ in range(v)]

    # se o grafo for não direcionado
    for _ in range(e):
        U, V, peso = map(int, input().split())
        # como é não direcionado, a aresta é bidirecional (de a para b e de b para a)
        grafo[U - 1].append((V, peso))
        grafo[V - 1].append((U, peso))

    mostrar_grafo(grafo)

    inicio = int(input("\nDigite o vértice inicial: ")) - 1
    aresta_excluida = tuple(map(int, input("\nDigite a aresta a ser excluída (no formato 'u v'): ").split()))
    
    # ajusta para índices base 0
    aresta_excluida = (aresta_excluida[0] - 1, aresta_excluida[1] - 1)
    
    distancias = dijkstra(grafo, inicio, aresta_excluida)

    print("\nDistâncias mais curtas a partir do vértice inicial\n")
    for i, distancia in enumerate(distancias):
        print(f"Vértice {i + 1}: {'Inf' if distancia == float('inf') else distancia}")

if __name__ == "__main__":
    main()
