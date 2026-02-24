#Funcionando perfeitamente conforme o Exercicio.

def atribuir_equipes(qt):
    base = []
    times = []
    fatecs = []
    tentativas = []
    tempo = []
    for _ in range(qt):
        time, fatec = input().split('|')
        processo = list(map(int, input().split(' ')))
        times.append(time)
        fatecs.append(fatec)
        tentativas.append([x for x in processo[0::2]])
        tempo.append([x for x in processo[1::2]])
    base.append(times)
    base.append(fatecs)
    base.append(tentativas)
    base.append(tempo)
    return base

def calculo(tentativas, tempo):
    score = []
    for i, equipe in enumerate(tentativas):
        acertos = 0
        scr_tempo = 0
        for j, tent in enumerate(equipe):
            if tent > 0 and tempo[i][j] > 0:
                acertos +=1
                scr_tempo += tempo[i][j] + (20 * (tent-1))
            else:
                continue
        score.append([acertos,scr_tempo])
    return score

def base_reduzida(base):
    base_ajustada = []
    for i in range(len(base[0])):
        base_ajustada.append([base[0][i],base[1][i],base[4][i]])
    return base_ajustada

def ranquear(base):
    ranqueado = sorted(base, key=lambda x: (-x[2][0], x[2][1], x[0]))
    return ranqueado

def exibir_resultado(base):
    for time, fatec, score in base:
        print(f'{time} - {fatec} ({score[0]},{score[1]})')

def menu():
    np = int(input())
    qt = int(input())
    dados = atribuir_equipes(qt)
    score = calculo(dados[2],dados[3])
    dados.append(score)
    dados_reduzidos = base_reduzida(dados)
    ranqueado = ranquear(dados_reduzidos)
    exibir_resultado(ranqueado)

menu()