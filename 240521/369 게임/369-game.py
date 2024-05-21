n = int(input())

# 1300은 틀림

for  i in range(1, n+1):
    if(i <= n // 100):
        if(i % 3 == 0):
            print(0, end=' ')     
        else:     
            print(i, end=' ')
    while(i > n // 100):
        q = i // 10
        r = i % 10

        if(i % 3 == 0):
            print(0, end=' ')
        elif(q == 3 or q == 6 or q == 9):
            print(0, end=' ')
        elif(r == 3 or r == 6 or r == 9):
            print(0, end=' ')
        else:
            print(i, end=' ')
        i = i // 100