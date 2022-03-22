"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    dic = {}
    
    for cc, email in log:
        if email in dic:
            dic[email] = ccMatcher(cc, dic[email])
        else:
            dic[email] = cc
    
    return sorted([(v, k) for k, v in dic.items()], key = lambda x: (x[0].count('*'), x[1]))
    
def ccMatcher(cc1, cc2):
    res = ""
    
    for i in range(0, 16):
        if cc2[i] != '*' and cc1[i] == '*':
            res += cc2[i]
        elif cc2[i] == '*' and cc1[i] != '*':
            res += cc1[i]
        elif cc2[i] != '*' and cc1[i] != '*':
            res += cc1[i]
        else:
            res += '*'
    
    return res
