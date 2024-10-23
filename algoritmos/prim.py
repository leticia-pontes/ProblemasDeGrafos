import timeit

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

def prim(grafo, inicio=0):
    arvore_geradora_minima = []
    visitados = [inicio]

    vizinhos = sorted([(inicio, adjacente, peso) for adjacente, peso in grafo[inicio]], key=lambda x: x[2])

    while len(visitados) < len(grafo):
        u, v, w = vizinhos.pop(0)

        if v not in visitados:
            arvore_geradora_minima.append((u, v, w))
            visitados.append(v)

            for adjacente, peso in grafo[v]:
                if adjacente not in visitados:
                    vizinhos.append((v, adjacente, peso))

            vizinhos = sorted(vizinhos, key=lambda x: x[2])

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

    tempo_prim = timeit.timeit(lambda: prim(grafo), number=1000)
    print(f"\nTempo médio de execução do algoritmo de Prim (1000 execuções): {tempo_prim:.6f} segundos\n")

if __name__ == '__main__':
    main()