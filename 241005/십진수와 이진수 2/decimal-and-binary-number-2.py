n = int(input())

l = []

while(n != 0):
    q = n // 10
    r = n % 10
    l.append(r)
    n = q

l.reverse()

total = 0

for num in l:
    total = 2 * total + int(num)

total *= 17

l.clear()

while(total != 0):
    q = total // 2
    r = total % 2
    l.append(r)
    total = q

l.reverse()

for num in l:
    print(num, end='')