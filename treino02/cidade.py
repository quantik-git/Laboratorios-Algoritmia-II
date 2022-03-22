'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.
'''
 
def tamanho(ruas):
    floydTable = fw(build(ruas))
    width = 0
    
    for orig, adjDict in floydTable.items():
        floydTable[orig] = sorted([dist for dest, dist in adjDict.items()])[-1]
        for dest, dist in adjDict.items():
            width = max(width, dist)
    
    return width

def build(ruas):
    adj = {}
    for rua in ruas:
        o = rua[0]
        d = rua[-1]
        p = len(rua)
        
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        
        if(d in adj[o] and p > adj[o][d]):
            continue;
        
        adj[o][d] = p
        adj[d][o] = p
    return adj

def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist
