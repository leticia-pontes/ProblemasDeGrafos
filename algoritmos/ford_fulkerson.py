from collections import deque

# verifica se há um caminho aumentante usando BFS
def bfs(grafo, fluxo, fonte, sumidouro, pais):
    visitado = [False] * len(grafo)
    queue = deque([fonte])
    visitado[fonte] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(len(grafo)):
            # se a capacidade residual é positiva e o vértice ainda não foi visitado
            if not visitado[v] and grafo[u][v] - fluxo[u][v] > 0:
                # atualiza o pai de v e marca como visitado
                pais[v] = u
                visitado[v] = True
                
                # se chegou no sumidouro, pode parar a busca
                if v == sumidouro:
                    return True
                queue.append(v)
    
    return False

def ford_fulkerson(grafo, fonte, sumidouro):
    # inicializa a matriz de fluxo com zeros
    fluxo = [[0] * len(grafo) for _ in range(len(grafo))]
    
    # inicializa a variável para armazenar o fluxo máximo
    fluxo_maximo = 0
    
    # armazena o caminho de pais para reconstruir o caminho aumentante
    pais = [-1] * len(grafo)
    
    # enquanto houver um caminho aumentante
    while bfs(grafo, fluxo, fonte, sumidouro, pais):
        # encontra a capacidade mínima ao longo do caminho aumentante
        caminho_fluxo = float('Inf')
        v = sumidouro
        
        while v != fonte:
            u = pais[v]
            caminho_fluxo = min(caminho_fluxo, grafo[u][v] - fluxo[u][v])
            v = u
        
        # atualiza os fluxos nas arestas do caminho aumentante
        v = sumidouro
        while v != fonte:
            u = pais[v]
            fluxo[u][v] += caminho_fluxo
            fluxo[v][u] -= caminho_fluxo
            v = u
        
        # adiciona o fluxo do caminho ao fluxo máximo
        fluxo_maximo += caminho_fluxo
    
    return fluxo_maximo

def main():
    grafo = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    fonte = 0
    sumidouro = 5

    fluxo_maximo = ford_fulkerson(grafo, fonte, sumidouro)
    print(f"Fluxo Máximo: {fluxo_maximo}")

if __name__ == '__main__':
    main()