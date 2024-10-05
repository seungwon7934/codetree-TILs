n, b = map(int, input().split())

l = []

while(n != 0):
    q = n // b
    r = n % b
    l.append(r)
    n = q

l.reverse()

for num in l:
    print(num, end='')