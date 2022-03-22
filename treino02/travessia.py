'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''

def travessia(mapa):
    maxY = len(mapa)
    maxX = len(mapa[0])
    is_valid = lambda x, y: (maxY > y >= 0 and maxX > x >= 0)
    short = (0, maxY * maxX)
    
    for i in range(0, maxX):
        vis = set()
        queue = [(i, 0, 0)]
        
        for ox, oy, custo in queue:
            if (ox, oy) in vis:
                continue
            
            if oy == (maxY-1):
                if custo < short[1]:
                    short = (i, custo)
            
            vis.add((ox, oy))
            vizinhos = [(ox+1, oy, 1), (ox-1, oy, 1), (ox, oy+1, 1), (ox, oy-1, 1)]
            
            for x, y, c in vizinhos:
                if(is_valid(x, y) and abs(int(mapa[y][x]) - int(mapa[oy][ox])) <= 2):
                    queue.append((x, y, (custo + c + abs(int(mapa[y][x]) - int(mapa[oy][ox])))))
    
    return short
