'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''
#incompleto 8%
def repete(palavra, n):
    res = palavra
    
    for i in range(1, len(palavra)):
        if (palavra[-i:] + palavra[i:]) == palavra:
            res = palavra[i:]
    
    return palavra + res*(n-1)
