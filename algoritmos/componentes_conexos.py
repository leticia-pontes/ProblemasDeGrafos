def dfs(grafo, inicio, visitados):
    
    visitados.add(inicio)

    for vizinho in grafo[inicio]:

        if vizinho not in visitados:    
            dfs(grafo, vizinho, visitados)

def componentes_conexos(grafo):

    visitados = set()
    componentes = []
    
    for vertice in grafo:
    
        if vertice not in visitados:
            componente = set()
    
            dfs(grafo, vertice, componente)
    
            componentes.append(componente)
            visitados.update(componente)
    
    return componentes

# Exemplo de grafo
grafo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['E'],
    'E': ['D']
}

componentes = componentes_conexos(grafo)

print("Componentes conectados:", componentes)
