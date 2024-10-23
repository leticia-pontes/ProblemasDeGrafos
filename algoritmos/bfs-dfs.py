from collections import deque

def bfs(grafo, inicio):
    """
    Executa a busca em largura (BFS) em um grafo a partir de um vértice inicial.
    Retorna um conjunto com os vértices visitados.
    """
    visitados = set()  # Conjunto para armazenar os vértices visitados
    fila = deque([inicio])  # Fila para processar os vértices a serem visitados
  
    visitados.add(inicio)  # Marca o vértice inicial como visitado
  
    while fila:
        v = fila.popleft()  # Remove o primeiro vértice da fila
  
        # Percorre os vizinhos do vértice atual
        for vizinho in grafo[v]:
            if vizinho not in visitados:
                visitados.add(vizinho)  # Marca o vizinho como visitado
                fila.append(vizinho)  # Adiciona o vizinho à fila para explorar
  
    return visitados  # Retorna o conjunto de vértices visitado

def dfs(grafo, vertice, visitado, lista_dfs):
    visitado[vertice] = True
  
    lista_dfs.append(vertice)
  
    for vizinho in grafo[vertice]:
        if not visitado[vizinho]:
            dfs(grafo, vizinho, visitado, lista_dfs)
  
# Grafo representado como uma lista de adjacências
grafo = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 4, 6],
    3: [1, 4],
    4: [2, 3],
    5: [6, 7],
    6: [2, 5, 7],
    7: [5, 6, 8],
    8: [7, 9],
    9: [8]
}

lista_bfs = bfs(grafo, 2)
print([x for x in lista_bfs])
  
visitado = [False] * len(grafo)
lista_dfs = []
  
dfs(grafo, 0, visitado, lista_dfs)
print(lista_dfs)