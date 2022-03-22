'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''
#[("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
#[('Porto', 4), ('Benfica', 4), ('Sporting', 2)]

def tabela(jogos):
    casa = {jogo[0] for jogo in jogos}
    opositores = {jogo[2] for jogo in jogos}
    tabela = {equipa: [0,0] for equipa in (casa | opositores)}
    
    for e1, g1, e2, g2 in jogos:
        tabela[e1] = update_golos(tabela[e1], (g1-g2))
        tabela[e2] = update_golos(tabela[e2], (g2-g1))
        if g1 > g2:
            update_pontos(tabela[e1], 3)
        elif g2 > g1:
            update_pontos(tabela[e2], 3)
        else:
            update_pontos(tabela[e1], 1)
            update_pontos(tabela[e2], 1)
            
    res = [(equipa, dados[0]) for equipa, dados in tabela.items()]
    
    return sorted(res, key = lambda x : (-x[1], -(tabela[x[0]])[1], x[0]))

def update_golos(entrada, val):
    entrada[1] += val
    return entrada

def update_pontos(entrada, val):
    entrada[0] += val
    return entrada
