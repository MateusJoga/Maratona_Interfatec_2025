#Funcionando perfeitamente conforme o Exercicio.

num = int(input())
valor = 1

def analisador(valor):
    lista = []
    caract = str(valor)
    conj = ''

    for c in caract:
        if not conj or c == conj[-1]:
            conj += c
        else:
            lista.append(conj)
            conj = c
    lista.append(conj)

    novo = ''
    for con in lista:
        novo += str(len(con)) + str(con[0])
    return novo

for _ in range(num-1):
    valor = analisador(valor)

print(valor)