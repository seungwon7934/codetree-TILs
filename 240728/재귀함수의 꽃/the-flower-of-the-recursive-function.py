def a(n):
    if(n == 0):
        return
    print(n,end=' ')
    a(n-1)
    print(n,end=' ')


n = int(input())

a(n)