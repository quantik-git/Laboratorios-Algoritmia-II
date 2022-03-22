'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''
# Euclides > Eratóstenes

def factoriza(n):
    primos = []
    while n > 1:
        print(n)
        for i in range(2, n+1):
            if n % i == 0:
                if i not in primos:
                    primos.append(i)
                n = n // i
                break
    
    return sum(primos)


def factoriza1(n):
    primos = primosAte(n)
    
    return sum(primos)
    
def primosAte(n):
    upper = (n//2)+2
    lista = [1]*(upper)
    res = []
    
    for i in range(2, upper):
        if(lista[i] == 1):
            for j in range(2*i, upper, i):
                lista[j] = 0
    
    for i in range(2, upper):
        if(lista[i] == 1 and n % i == 0):
            res.append(i)
    
    return res
