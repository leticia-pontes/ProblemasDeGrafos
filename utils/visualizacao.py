
def mostrar_lista_adjacencias(grafo):
    for vertice, adjacentes in grafo.items():
        print(vertice, end=': ')
        print(adjacentes)
