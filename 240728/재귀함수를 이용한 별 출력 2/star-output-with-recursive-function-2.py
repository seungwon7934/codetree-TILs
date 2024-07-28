def a(n):
    if(n == 0):
        return
    for _ in range(n):
        print("*",end=' ')
    print()
    a(n-1)
    for _ in range(n):
        print("*",end=' ')
    print()

n = int(input())

a(n)