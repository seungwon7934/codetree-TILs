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

print(total)