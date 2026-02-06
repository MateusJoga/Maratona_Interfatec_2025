#Funcionando perfeitamente conforme solicitado no Exercício.

def intervalo(valor):
    busca = 1
    resultado = busca ** busca
    while valor >= resultado:
        busca += 1
        resultado = busca ** busca
        if valor == resultado:
            return busca, busca
    return busca-1, busca

def HS(min, max):
    hs = (min + max)/2
    return hs

def ND(hs):
    nd = hs ** hs
    return nd

def calcular_tempo(valor, min, max):
    hs = HS(min, max)
    nd = ND(hs)
    dif = nd - valor
    if dif < -0.001:
        val = calcular_tempo(valor, hs, max)
    elif dif > 0.001:
        val = calcular_tempo(valor, min, hs)
    else:
        return hs
    return val
    
def transformar(valor):
    horario = valor * 60
    minuto = horario // 60
    resto = horario % 60
    segundos, milesimos = str(resto).split('.')
    if len(segundos) < 2:
        segundos = '0'+segundos
    if len(milesimos) < 3:
        milesimos = '0'*(3-len(milesimos))+milesimos
    return f'{minuto:.0f}:{segundos}:{milesimos[0:3]}'

while True:
    entrada = float(input())
    if entrada == 0:
        break
    minimo, maximo = intervalo(entrada)
    print(minimo, maximo)
    tempo = calcular_tempo(entrada, minimo, maximo)
    print(transformar(tempo))
    