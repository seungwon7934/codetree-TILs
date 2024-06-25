n = int(input())

for i in range(1, n * 2):
    if(i <= n):
        for j in range(i):
            print("* ", end='')
        print()
    else:
        for j in range(i - n, n):
            print("* ", end='')
        print()