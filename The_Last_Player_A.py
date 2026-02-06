#Funcionando perfeitamente conforme solicitado.

n, k = map(int, input().split(' '))

jogadores = [i for i in range(1,n+1)]
eliminados = []
sobra = jogadores

kcont = 0

while len(sobra) != 1:
    for i in sobra:
        kcont += 1
        if kcont == k:
            eliminados.append(i)
            kcont = 0        
    sobra = list(set(jogadores).difference(eliminados))

print(f'{sobra[0]}')