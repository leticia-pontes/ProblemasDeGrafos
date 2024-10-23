import timeit

def ordenar_arestas_por_peso(grafo):
    arestas = []
    
    for vertice, adjacencias in grafo.items():
        for adjacente, peso in adjacencias:
            arestas.append((vertice, adjacente, peso))

    arestas_ordenadas = sorted(arestas, key=lambda x: x[2])

    return arestas_ordenadas

def encontrar_componente(vertice, componentes):
    """Encontra o componente a que o vértice pertence"""
    for componente in componentes:
        if vertice in componente:
            return componente
    return None

def converter_para_lista_adjacencias(arestas):
    lista_adjacencias = {}
    
    for v1, v2, peso in arestas:
        if v1 not in lista_adjacencias:
            lista_adjacencias[v1] = []
        if v2 not in lista_adjacencias:
            lista_adjacencias[v2] = []
        
        lista_adjacencias[v1].append((v2, peso))
        lista_adjacencias[v2].append((v1, peso))
    
    return lista_adjacencias

def kruskal(grafo):
    arvore_geradora_minima = []
    arestas_ordenadas = ordenar_arestas_por_peso(grafo)

    componentes = [[v] for v in grafo.keys()]
    
    for aresta in arestas_ordenadas:
        v1, v2, peso = aresta

        componente_v1 = encontrar_componente(v1, componentes)
        componente_v2 = encontrar_componente(v2, componentes)

        if componente_v1 != componente_v2:
            arvore_geradora_minima.append((v1, v2, peso))

            componentes.remove(componente_v1)
            componentes.remove(componente_v2)

            componentes.append(componente_v1 + componente_v2)

    lista_adjacencias = converter_para_lista_adjacencias(arvore_geradora_minima)
    
    print("\nArestas da Árvore Geradora Mínima:\n")
    for aresta in arvore_geradora_minima:
        print(aresta)

    print("\nLista de Adjacências da Árvore Geradora Mínima:\n")
    for vertice in sorted(lista_adjacencias.keys()):
        adjacentes = lista_adjacencias[vertice]
        print(f"{vertice}: {sorted(adjacentes)}")

def mostrar_lista_adjacencias(grafo):
    for vertice, adjacentes in grafo.items():
        print(vertice, end=': ')
        print(adjacentes)

def main():
    grafo = {
        0: [(3, 4), (2, 4)],
        1: [(3, 2), (6, 10), (4, 4), (2, 7), (6, 6), (0, 2), (5, 3)],
        2: [(3, 1), (5, 5)],
        3: [(0, 4), (2, 1), (1, 2), (7, 10)],
        4: [(1, 4), (5, 1), (3, 3), (1, 2)],
        5: [(4, 1), (4, 4)],
        6: [(1, 10), (5, 3)],
        7: [(3, 10), (1, 6), (0, 3), (1, 4), (3, 5)]
    }

    print('\nGrafo:\n')
    mostrar_lista_adjacencias(grafo)

    tempo_kruskal = timeit.timeit(lambda: kruskal(grafo), number=1000)
    print(f"\nTempo médio de execução do algoritmo de Kruskal (1000 execuções): {tempo_kruskal:.6f} segundos\n")

if __name__ == '__main__':
    main()