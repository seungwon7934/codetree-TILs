def p(n):
    if(n == 0):
        return
    print(n,end=' ')
    p(n-1)

def q(n):
    if(n == 0):
        return
    print(8-n,end=' ')
    q(n-1)

n = int(input())

q(n)
print()
p(n)