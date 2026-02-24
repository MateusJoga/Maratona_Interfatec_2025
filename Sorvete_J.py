#Funcionando perfeitamente conforme solicitado no Exercício.

clientes, dif = map(int, input().split(' '))
temperaturas = []

for i in range(clientes):
    temp = int(input())
    temperaturas.append(temp)

temperaturas.sort()

def separador(temperatura):
    valor = temperatura[0]
    grupos = 1
    for i in temperatura:
        if i > valor + dif:
            grupos += 1
            valor = i
    return grupos

print(separador(temperaturas))