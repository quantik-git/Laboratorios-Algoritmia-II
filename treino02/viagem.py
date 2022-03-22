'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

10%

está a dar o caminho mais curto mas acho que pode haver um mais longo com custo menor 
'''

def viagem(rotas,o,d):
    arestas = []
    cheapest = float("inf")
    
    for rota in rotas:
        while len(rota) > 1:
            arestas.append((rota[0], rota[2], rota[1]))
            rota = rota[2:]
    
    adj = build(arestas)
    
    queue = [(o, 0)]
    vis = set()
    
    for rota, preco in queue:
        if rota in vis:
            continue
        
        if rota == d:
            if preco < cheapest:
                cheapest = preco
            continue
        
        vis.add(rota)
        nrotas = adj[rota]
        
        for destino, custo in nrotas.items():
            queue.append((destino, preco+custo))
    
    return cheapest


def build(arestas):
    adj = {}
    for o, d, p in arestas:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        
        if(d in adj[o] and p > adj[o][d]):
            continue;
        
        adj[o][d] = p
        adj[d][o] = p
    return adj
