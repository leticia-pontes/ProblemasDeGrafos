import matplotlib.pyplot as plt
import networkx as nx

def desenharGrafo(G, arvore, filtro):
    position = nx.spring_layout(G, seed=1)

    # Nós
    nx.draw_networkx_nodes(G, position, node_size=1000, node_color="#df1530")

    match (filtro):
        case 1:
            # Defaut
            nx.draw_networkx_edges(G, position, width=6, edge_color="#113ac5")
            nx.draw_networkx_labels(G, position, font_size=20, font_family="sans-serif", font_color="white", font_weight="bold")
            edge_labels = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(G, position, edge_labels, font_size=15, font_family="sans-serif", font_weight="bold")

        case 2:
            # Destaque
            nx.draw_networkx_edges(G, position, width=6, edge_color="#113ac5")
            nx.draw_networkx_labels(G, position, font_size=20, font_family="sans-serif", font_color="white", font_weight="bold")
            
            arvore_edges = [(aresta.origem, aresta.destino) for aresta in arvore]
            nx.draw_networkx_edges(G, position, edgelist=arvore_edges, width=6, edge_color="#df1530")  # Destaque para a AGM
            
            edge_labels = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(G, position, edge_labels, font_size=15, font_family="sans-serif", font_weight="bold")

        case 3:
            # Apenas Arvore
            arvore_edges = [(aresta.origem, aresta.destino) for aresta in arvore]
            nx.draw_networkx_edges(G, position, edgelist=arvore_edges, width=6, edge_color="#df1530")

            arvore_labels = set([aresta.origem for aresta in arvore] + [aresta.destino for aresta in arvore])
            labels_arvore = {n: n for n in arvore_labels}
            nx.draw_networkx_labels(G, position, labels=labels_arvore, font_size=20, font_family="sans-serif", font_color="white", font_weight="bold")

            arvore_weight_labels = {(aresta.origem, aresta.destino): aresta.peso for aresta in arvore}
            nx.draw_networkx_edge_labels(G, position, edge_labels=arvore_weight_labels, font_size=15, font_family="sans-serif", font_weight="bold")

    plt.tight_layout()
    plt.show()

class Subconjunto:
    def __init__(self, pai, classificacaoKey):
        self.pai = pai
        self.classificacaoKey = classificacaoKey

class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso

def procurarKruskal(arestas):
    arvore = []
    subconjuntos = []

    def numerosDeNos(arestas):
        nos = []
        for aresta in arestas:
            nos.append(aresta.origem)
            nos.append(aresta.destino)
        return len(nos)

    n = numerosDeNos(arestas)

    def procurar(subconjuntos, i):
        if subconjuntos[i].pai != i:
            subconjuntos[i].pai = procurar(subconjuntos, subconjuntos[i].pai)
        return subconjuntos[i].pai

    def unir(subconjuntos, no1, no2):
        no1 = procurar(subconjuntos, no1)
        no2 = procurar(subconjuntos, no2)

        if subconjuntos[no1].classificacaoKey < subconjuntos[no2].classificacaoKey:
            subconjuntos[no1].pai = no2
        elif subconjuntos[no1].classificacaoKey > subconjuntos[no2].classificacaoKey:
            subconjuntos[no2].pai = no1
        else:
            subconjuntos[no2].pai = no1
            subconjuntos[no1].classificacaoKey += 1

    arestas.sort(key=lambda x: x.peso)

    for i in range(n):
        subconjuntos.append(Subconjunto(i, 0))

    i = 0
    while len(arvore) < n - 1 and i < len(arestas):
        aresta = arestas[i]

        noPrimario = procurar(subconjuntos, aresta.origem)
        noFinal = procurar(subconjuntos, aresta.destino)

        if noPrimario != noFinal:
            arvore.append(aresta)
            unir(subconjuntos, noPrimario, noFinal)

        i += 1

    return arvore

def procurarPrim(arestas, noInicial):
    grafo = {}
    for aresta in arestas:
        if aresta.origem not in grafo:
            grafo[aresta.origem] = []
        if aresta.destino not in grafo:
            grafo[aresta.destino] = []
        grafo[aresta.origem].append((aresta.peso, aresta.destino))
        grafo[aresta.destino].append((aresta.peso, aresta.origem))

    arvore = []
    noVisitado = []
    noProximo = []

    noVisitado.append(noInicial)
    for peso, destino in grafo[noInicial]:
        noProximo.append((peso, noInicial, destino))

    while noProximo:
        menorAresta = min(noProximo, key=lambda x: x[0])
        peso, origem, destino = menorAresta

        noProximo.remove(menorAresta)

        if destino not in noVisitado:
            noVisitado.append(destino)
            arvore.append(Aresta(origem, destino, peso))

            for prox_peso, prox_destino in grafo[destino]:
                if prox_destino not in noVisitado:
                    noProximo.append((prox_peso, destino, prox_destino))

    return arvore

def main():
    # Para amostragem
    G = nx.Graph()
    G.add_edge(4,5, weight=35)
    G.add_edge(4,7, weight=37)
    G.add_edge(5,7, weight=28)
    G.add_edge(0,7, weight=16)
    G.add_edge(1,5, weight=32)
    G.add_edge(0,4, weight=38)
    G.add_edge(2,3, weight=17)
    G.add_edge(1,7, weight=19)
    G.add_edge(0,2, weight=26)
    G.add_edge(1,2, weight=36)
    G.add_edge(1,3, weight=29)
    G.add_edge(2,7, weight=34)
    G.add_edge(6,2, weight=40)
    G.add_edge(3,6, weight=52)
    G.add_edge(6,0, weight=58)
    G.add_edge(6,4, weight=93)
    # Para conta
    arestas = [
        Aresta(4,5,35),
        Aresta(4,7,37),
        Aresta(5,7,28),
        Aresta(0,7,16),
        Aresta(1,5,32),
        Aresta(0,4,38),
        Aresta(2,3,17),
        Aresta(1,7,19),
        Aresta(0,2,26),
        Aresta(1,2,36),
        Aresta(1,3,29),
        Aresta(2,7,34),
        Aresta(6,2,40),
        Aresta(3,6,52),
        Aresta(6,0,58),
        Aresta(6,4,93),
    ]

    arvoreKruskal = procurarKruskal(arestas)
    desenharGrafo(G, arvoreKruskal, 1)
    desenharGrafo(G, arvoreKruskal, 2)
    desenharGrafo(G, arvoreKruskal, 3)

    arvorePrim = procurarPrim(arestas, 1)
    desenharGrafo(G, arvorePrim, 1)
    desenharGrafo(G, arvorePrim, 2)
    desenharGrafo(G, arvorePrim, 3)



if __name__ == "__main__":
    main()
