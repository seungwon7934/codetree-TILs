n = int(input())

for i in range(n):
    for j in range(i * 2):
        print(" ",end='')

    for j in range(n * 2 - i * 2 - 1):
        print("* ", end='')
    print()