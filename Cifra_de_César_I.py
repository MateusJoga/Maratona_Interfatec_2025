#Funcionando perfeitamente conforme solicitado no Exercício.

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def verificador_desloc(texto):
    ultimos = texto[-3::]
    i1,i2,i3 = verificador_indice(ultimos[0]), verificador_indice(ultimos[1]), verificador_indice(ultimos[2])
    ver = alfabeto[i1-i1]+alfabeto[i2-i1]+alfabeto[i3-i1]
    if ver == 'AVE':
        return i1
    else:
        if i1 > 15:
            return i1-15
        else:
            return i1+11
        

def verificador_indice(letra, deslocador=0):
    for i, l in enumerate(alfabeto):
        if l == letra:
            return i-deslocador

while True:
    texto = str(input())
    if texto == '***':
        break
    desloc = verificador_desloc(texto)
    novo_texto = ''
    for l in texto:
        if l in alfabeto:
            indice = verificador_indice(l, desloc)
            novo_texto += alfabeto[indice]
        else:
            novo_texto += l

    print(novo_texto)