a, b = map(int, input().split())
n = int(input())
l = []
total = 0

while(n != 0):
    l.append(n % 10)
    n //= 10
l.reverse()

for m in l:
    total = a * total + int(m)

l.clear()

while(total != 0):
    l.append(total % b)
    total //= b
l.reverse()

for m in l:
    print(m,end='')