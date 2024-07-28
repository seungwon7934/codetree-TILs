def p(n):
    if(n == 0):
        return
    p(n-1)
    for _ in range(n):
        print("*",end='')
    print()

n = int(input())

p(n)