#Funcionando perfeitamente conforme solicitado no Exercício.

a,b,c = map(int, input().split(' '))

def valores(a, b, c):
    melhor = None
    for y in range(c//b +1):
        resto = c - y * b
        if resto < 0:
            break
        if resto % a == 0:
            x = resto // a
            total = x + y
            if melhor is None or total < melhor[0] or (total == melhor [0] and x < melhor[1]):
                melhor = (total, x, y)
    return melhor[1], melhor[2]
    
try:
    ponteA,ponteB = valores(a,b,c)
    print(f'{ponteA} {ponteB}')
except:
    print('IMPOSSIVEL')