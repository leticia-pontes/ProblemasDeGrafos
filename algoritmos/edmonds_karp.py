import time
import random
from collections import deque

class Grafo:
    def __init__(self, tamanho):
        self.matriz_adjacencias = [[0] * tamanho for _ in range(tamanho)]
        self.tamanho = tamanho
        self.dados_dos_vertices = [''] * tamanho

    def adicionar_aresta(self, u, v, c): # (inicial, final, capacidade)
        self.matriz_adjacencias[u][v] = c

    def adicionar_dados_dos_vertices(self, vertice, dado):
        if 0 <= vertice < self.tamanho:
            self.dados_dos_vertices[vertice] = dado

    def bfs(self, inicio, fim, capacidade_residual):
        """
        Executa a busca em largura (BFS) no grafo, a partir de um vértice inicial,
        para encontrar um caminho aumentante. Retorna uma lista de predecessores
        para reconstrução do caminho, se um caminho for encontrado, ou None se não houver caminho.
        """
        visitados = [False] * self.tamanho  # Marca os vértices como não visitados
        fila = deque([inicio])  # Fila para explorar os vértices
        predecessores = [-1] * self.tamanho  # Lista para armazenar os predecessores dos vértices
        """
        Predecessores são os vértices de onde podemos chegar a outro vértice em um grafo.
        Na busca em largura, o vértice de onde chegamos a outro é registrado
        para poder reconstruir o caminho depois.
        """

        visitados[inicio] = True  # Marca o vértice inicial como visitado

        while fila:
            v = fila.popleft()  # Remove o primeiro vértice da fila

            # Verifica todos os vizinhos do vértice v
            for vizinho in range(self.tamanho):
                if not visitados[vizinho] and capacidade_residual[v][vizinho] > 0:
                    fila.append(vizinho)
                    visitados[vizinho] = True
                    predecessores[vizinho] = v  # Marca o vértice v como predecessor do vizinho

                    # Se chegamos ao vértice final, podemos interromper a busca
                    if vizinho == fim:
                        return predecessores  # Retorna os predecessores para reconstrução do caminho

        return None  # Se não encontrar o caminho, retorna None

    def edmonds_karp(self, fonte, sumidouro):
        capacidade_residual = [row[:] for row in self.matriz_adjacencias]
        fluxo_maximo = 0  # Inicia o fluxo máximo com 0

        while True:
            predecessores = self.bfs(fonte, sumidouro, capacidade_residual)
            if predecessores is None:
                break

            # Determina o fluxo máximo que pode ser enviado pelo caminho encontrado
            fluxo_caminho = float("Inf")
            v = sumidouro
            while v != fonte:
                u = predecessores[v]
                fluxo_caminho = min(fluxo_caminho, capacidade_residual[u][v])
                v = u

            fluxo_maximo += fluxo_caminho

            # Atualiza as capacidades residuais
            v = sumidouro
            while v != fonte:
                u = predecessores[v]
                capacidade_residual[u][v] -= fluxo_caminho
                capacidade_residual[v][u] += fluxo_caminho
                v = u

            # Reconstroi o caminho e imprime o fluxo
            caminho = []
            v = sumidouro
            while v != fonte:
                caminho.append(v)
                v = predecessores[v]
            caminho.append(fonte)
            caminho.reverse()

            nomes_caminhos = [self.dados_dos_vertices[no] for no in caminho]
            print("Caminho:", " -> ".join(nomes_caminhos), ", Fluxo: ", fluxo_caminho)

        return fluxo_maximo


# Função para criar grafos pequenos, médios e grandes
def criar_grafo(tamanho_U, tamanho_V):
    """
    Cria um grafo bipartido com vértices em U e V, além de uma superfonte 's' e um superdreno 't'.
    As capacidades das arestas entre os vértices de U e V são geradas aleatoriamente.
    """
    g = Grafo(tamanho_U + tamanho_V + 2)  # +2 para superfonte e superdreno

    nomes_vertices = ['s'] + [f'U{i}' for i in range(1, tamanho_U + 1)] + [f'V{i}' for i in range(1, tamanho_V + 1)] + ['t']

    for i, nome in enumerate(nomes_vertices):
        g.adicionar_dados_dos_vertices(i, nome)

    # Arestas da superfonte para o conjunto U
    for u in range(1, tamanho_U + 1):
        g.adicionar_aresta(0, u, 1)  # Capacidades entre superfonte e U são iguais a 1

    # Arestas entre U e V com capacidades aleatórias
    for u in range(1, tamanho_U + 1):
        for v in range(1, tamanho_V + 1):
            capacidade = random.randint(1, 10)  # Capacidade aleatória entre 1 e 10
            g.adicionar_aresta(u, tamanho_U + v, capacidade)

    # Arestas do conjunto V para o superdreno
    for v in range(1, tamanho_V + 1):
        g.adicionar_aresta(tamanho_U + v, g.tamanho - 1, 1)  # Capacidades entre V e superdreno são iguais a 1

    return g


# Função para testar o desempenho
def testar_desempenho(tamanho_U, tamanho_V):
    grafo = criar_grafo(tamanho_U, tamanho_V)

    # Medir o tempo de execução
    start_time = time.time()
    fluxo_maximo = grafo.edmonds_karp(0, grafo.tamanho - 1)
    end_time = time.time()

    tempo_execucao = end_time - start_time
    print(f"\nTeste com {tamanho_U} vértices em U e {tamanho_V} vértices em V:")
    print(f"\nO número máximo de casamentos é: {fluxo_maximo}")
    print(f"Tempo de execução: {tempo_execucao:.6f} segundos\n")


# Teste do algoritmo de Edmonds-Karp
g = Grafo(6)
nomes_vertices = ['s', 'v1', 'v2', 'v3', 'v4', 't']
for i, nome in enumerate(nomes_vertices):
    g.adicionar_dados_dos_vertices(i, nome)

g.adicionar_aresta(0, 1, 3)  # s  -> v1, cap: 3
g.adicionar_aresta(0, 2, 7)  # s  -> v2, cap: 7
g.adicionar_aresta(1, 3, 3)  # v1 -> v3, cap: 3
g.adicionar_aresta(1, 4, 4)  # v1 -> v4, cap: 4
g.adicionar_aresta(2, 1, 5)  # v2 -> v1, cap: 5
g.adicionar_aresta(2, 4, 3)  # v2 -> v4, cap: 3
g.adicionar_aresta(3, 4, 3)  # v3 -> v4, cap: 3
g.adicionar_aresta(3, 5, 2)  # v3 -> t,  cap: 2
g.adicionar_aresta(4, 5, 6)  # v4 -> t,  cap: 6

fonte = 0; sumidouro = 5

start_time = time.time()
fluxo_maximo = g.edmonds_karp(fonte, sumidouro)
end_time = time.time()

print("\nO fluxo máximo possível (número máximo de casamentos) é %d " % fluxo_maximo)
print("Tempo de execução: %.6f segundos" % (end_time - start_time))


# Testar casamento máximo com grafos de diferentes tamanhos
testar_desempenho(182, 43)