'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    palavras = texto.split(' ')
    
    dic = {}
    
    for palavra in palavras:
        dic[palavra] = (dic[palavra] if palavra in dic else 0) + 1
            
    lista = list(dic.items())
    
    lista.sort()
    lista.sort(key = lambda a: a[1], reverse = True)
    
    
    return [k for k,v in lista]
