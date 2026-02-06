#Funcionando perfeitamente conforme solicitado no Exercício.

dict = {
    'V O': 1,
    '* V': 1,
    'O *': 1,
    'O V': -1,
    'V *': -1,
    '* O': -1,
}

ind = 0

while True:
    res = input()
    if res == '- -':
        break
    for key, val in dict.items():
        if res == key:
            ind = ind + val
        else:
            pass

if ind > 0:
    print('BEATRIZ WIN')
elif ind < 0:
    print('ARTUR WIN')
else:
    print('TIE')