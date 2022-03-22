"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""
def aloca(prefs):
    res = []
    blacklist = []
    lista = [(aluno, proj) for aluno, proj in prefs.items()]
    lista.sort()
    
    for elem in lista:
        projetos_possiveis = [el for el in elem[1] if el not in blacklist]
        if projetos_possiveis == []:
            res.append(elem[0])
        else:
            blacklist.append(projetos_possiveis[0])
    return res
