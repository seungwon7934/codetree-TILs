total = 0

a, b, c = map(int, input().split())

def d(n):
    if(n == 0):
        return
    global total
    q = n // 10
    r = n % 10
    total += r
    n = q
    d(n)

d(a * b * c)

print(total)