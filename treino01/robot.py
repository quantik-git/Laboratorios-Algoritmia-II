'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    res = []
    retangulo = (0,0,0,0)
    pos_atual = [0,0]
    direcao = 0
    
    for comando in comandos:
        if comando == 'E':
            direcao = (direcao - 1) % 4
        elif comando == 'D':
            direcao = (direcao + 1) % 4
        elif comando == 'A':
            if direcao == 0:
                pos_atual[1] += 1
            elif direcao == 1:
                pos_atual[0] += 1
            elif direcao == 2:
                pos_atual[1] -= 1
            elif direcao == 3:
                pos_atual[0] -= 1
        elif comando == 'H':
            res.append(retangulo)
            retangulo = (0,0,0,0)
            pos_atual = [0, 0]
            direcao = 0
            
        retangulo = (min(pos_atual[0], retangulo[0]), min(pos_atual[1], retangulo[1]), max(pos_atual[0], retangulo[2]), max(pos_atual[1], retangulo[3]))
    
    return res
