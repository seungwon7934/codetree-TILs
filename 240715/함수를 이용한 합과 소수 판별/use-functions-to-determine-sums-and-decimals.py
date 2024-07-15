def isPrime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def isEven(n):
    total = 0
    while(n != 0):
        q = n // 10
        r = n % 10
        total += r
        n = q
    if(total % 2 == 0):
        return True
    else:
        return False

a, b = map(int, input().split())
total = 0

for i in range(a, b+1):
    if(isPrime(i) and isEven(i)):
        total += 1

print(total)