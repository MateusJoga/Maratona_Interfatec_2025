a, b = map(int,(input().split(' ')))
dado = []
maior = [0,0]

for i in range(a,b+1):
    nums = list(str(i))
    res = 0
    for num in nums:
        res += int(num)
    dado.append((i, res))

for reg in dado:
    if reg[1] > maior[1]:
        maior[0] = reg[0]
        maior[1] = reg[1]
    else:
        continue

print(maior[0])
    