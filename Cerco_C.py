#Funcionando perfeitamente conforme solicitado no Exercício.

x,y,r = map(int, input().split(' '))
N = int(input())

xmenor = x - r
xmaior = x + r
ymenor = y - r
ymaior = y + r

sneakys = 0

def dentro(x,y):
    if x >= xmenor and x <= xmaior and y >= ymenor and y <= ymaior:
        return 1
    else:
        return 0


for _ in range(N):
    xi, ji = map(int, input().split(' '))
    sneakys += dentro(xi,ji)

print(sneakys)