'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    return sorted([k for k, v in livros.items() if isIsbn(v)])
    
def isIsbn(isbn):
    ones = [int(char) for char in list(isbn[0:13:2])]
    threes = [int(char)*3 for char in list(isbn[1:12:2])]
    
    return ((sum(ones) + sum(threes)) % 10) != 0
