'''
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
parceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

10%
'''

def erdos(artigos, n):
    adj = build(artigos)
    
    res = []
    
    queue = [('Paul Erdos', 0)]
    vis = set()
    
    for autor, erdos in queue:
        if autor in vis:
            continue
        
        vis.add(autor)
        res.append((autor, erdos))
        
        coautores = adj.get(autor, [])
        
        for coautor in coautores:
            if erdos < n:
                queue.append((coautor, erdos+1))
    
    res.sort(key = lambda x : (x[1], x[0]))
    
    return [author for author, erdos in res]

def build(artigos):
    adj = {}
    
    for artigo, autores in artigos.items():
        while autores:
            o = autores.pop()
            for d in autores:
                if o not in adj:
                    adj[o] = set()
                if d not in adj:
                    adj[d] = set()
                
                adj[o].add(d)
                adj[d].add(o)
    return adj
