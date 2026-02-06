#EXERCICIO INCOMPLETO

for

'''
N = numero total de cidades
M = numero de estradas
K = numero maximo de estradas vigiadas permitidas
R = numero de cidades pertencentes à Cypria
'''
N, M, K, R = int(input().split())

cidCypria = set(map(int, input().split()))
cidades = {}
for i in range(N):
    cidades[i] = {
        'Cypria': False if i not in cidCypria else True
    }

'''
S = cidade inicial
T = cidade destino
'''
S, T = int(input().split())

'''
U,V = cidades conectadas
W = tempo de viagem
P = 0 se estrada é segura, 1 se estrada tem vigilancia Sneaky
'''
for _ in range(M):
    U, V, W, P = map(int, input().split())
    cidades[U]['Estradas'] = {
        'Tempo': W,
        'Vigiada': P
    }