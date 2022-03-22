'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    cruzamentos = {}
    
    for rua in ruas:
        c1 = rua[0]
        c2 = rua[-1]
        if c1 not in cruzamentos and c1 != c2:
            cruzamentos[c1] = 1
        elif c1 != c2:
            cruzamentos[c1] = cruzamentos[c1] + 1
        if c2 not in cruzamentos:
            cruzamentos[c2] = 1
        else:
            cruzamentos[c2] = cruzamentos[c2] + 1
    
    res = cruzamentos.items()
    
    return sorted(res, key = lambda x : (x[1], x[0]))
