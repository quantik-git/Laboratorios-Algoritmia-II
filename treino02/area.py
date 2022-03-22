'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def area(p,mapa):
    maxY = len(mapa)
    maxX = len(mapa[0])
    is_valid = lambda x, y: (maxY > y >= 0 and maxX > x >= 0 and mapa[y][x] == ".")
    
    stack = []
    vis = set()
    
    stack.append(p)
    
    while stack != []:
        (x, y) = stack.pop()
        
        if (x, y) not in vis:
            vis.add((x, y))
        else:
            continue
        
        vizinhos = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        for x, y in vizinhos:
            if(is_valid(x, y)):
                stack.append((x, y))
    
    return len(vis)
