
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