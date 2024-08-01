def f(n):
    if(n == 1):
        return n
    return n * f(n-1)

n = int(input())

print(f(n))