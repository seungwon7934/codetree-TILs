n = int(input())
total = 0

while(n != 0):
    q = n // 10
    r = n % 10
    total += r
    n = q
print(total)