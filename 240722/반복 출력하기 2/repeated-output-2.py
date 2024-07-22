def p(n):
    if(n == 0):
        return
    else:
        print("HelloWorld")
        p(n-1)


n = int(input())
p(n)