'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def maior(vizinhos):
    res = 0
    componentes = [set(fronteiras) for fronteiras in vizinhos]
    
    while componentes:
        comp = componentes.pop()
        flag = 0
        
        for componente in componentes:
            if comp & componente:
                componente.update(comp)
                flag = 1
                break
        
        if not flag:
            cardinalidade = len(comp)
            if cardinalidade > res:
                res = cardinalidade
    
    return res
