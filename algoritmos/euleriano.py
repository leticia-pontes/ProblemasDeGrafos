from collections import deque

# BFS para verificar se o grafo é conexo
def bfs(grafo, inicio=0):
    visitados = {inicio}
    fila = deque([inicio])

    while fila:
        vertice = fila.popleft()
        for vizinho in grafo[vertice]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                
    return visitados


def verifica_grafo_conexo(grafo):
    return len(bfs(grafo)) == len(grafo)


def verifica_caminho(grafo, vertice_inicial=0):
    arestas_visitadas = set()
    caminho = []
    fila = [vertice_inicial]

    # Usando uma cópia do grafo para não alterar o original
    grafo = [list(vizinhos) for vizinhos in grafo]

    while fila:
        vertice_atual = fila[-1]
        if grafo[vertice_atual]:
            proximo_vertice = grafo[vertice_atual].pop()
            aresta = (vertice_atual, proximo_vertice)
            aresta_inversa = (proximo_vertice, vertice_atual)

            if aresta not in arestas_visitadas and aresta_inversa not in arestas_visitadas:
                arestas_visitadas.add(aresta)
                fila.append(proximo_vertice)
        else:
            caminho.append(fila.pop())

    return caminho


def calcula_numero_arestas(grafo):
    return sum(len(v) for v in grafo) // 2


def verifica_grau_impar(grafo):
    return sum(1 for vertice in grafo if len(vertice) % 2 != 0)


# Grafos de exemplo
grafo_euleriano = [
    [1, 6],
    [0, 2],
    [1, 3],
    [2, 4],
    [3, 5],
    [4, 6],
    [0, 5]
]

grafo_nao_euleriano = [
    [1, 2],
    [0, 2, 3],
    [0, 1],
    [1, 4, 5],
    [3, 5],
    [3, 4, 6],
    [5]
]

# verificação de grafo euleriano
def verifica_euleriano(grafo):
    if not verifica_grafo_conexo(grafo):
        return "Não é um grafo euleriano"
    
    num_impares = verifica_grau_impar(grafo)
    
    if num_impares == 0 or num_impares == 2:
        caminho = verifica_caminho(grafo, 0)
        return "É um grafo euleriano" if len(caminho) - 1 == calcula_numero_arestas(grafo) else "Não é um grafo euleriano"
    
    return "Não é um grafo euleriano"


print(verifica_euleriano(grafo_euleriano))
print(verifica_euleriano(grafo_nao_euleriano))
