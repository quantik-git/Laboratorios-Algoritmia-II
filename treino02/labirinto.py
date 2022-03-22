'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

  N
O . E
  S

'''

def caminho(mapa):
    maxY = len(mapa)
    maxX = len(mapa[0])
    is_valid = lambda x, y: (maxY > y >= 0 and maxX > x >= 0 and mapa[y][x] == " ")
    stack = []
    vis = set()
    
    stack.append((0, 0, ''))
    
    for x, y, mov in stack:
        
        if (x, y) in vis:
            continue
        
        if x == (maxX-1) and y == (maxY-1):
            return mov
        
        vis.add((x, y))
        vizinhos = [(x+1, y, 'E'), (x-1, y, 'O'), (x, y+1, 'S'), (x, y-1, 'N')]
        
        for x, y, m in vizinhos:
            if(is_valid(x, y)):
                stack.append((x, y, (mov + m)))
        
    return "NSEO"
