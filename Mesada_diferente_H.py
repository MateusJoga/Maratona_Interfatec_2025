#Funcionando perfeitamente conforme solicitado no Exercício.

filho, mesada, cat = map(int, input().split(' '))
tabela = []
total = 0
valor = (mesada / filho) // 10

for i in range(filho):
    categorias = [0 for _ in range(cat)]
    tabela.append(categorias)

for i, cont in enumerate(tabela):
    if i == filho-1:
        mesa = mesada - total
    else:
        mesa = valor * 10
    total += mesa
    for ind in range(len(cont)):
        if mesa >= 30:
            tabela[i][ind] = 30
            mesa -= 30
        elif mesa >= 20:
            tabela[i][ind] = 20
            mesa -= 20
        elif mesa >=10:
            tabela[i][ind] = 10
            mesa -= 10
        else:
            continue

for i in tabela:
    print(*(f'{i[x]}' for x in range(len(i))))