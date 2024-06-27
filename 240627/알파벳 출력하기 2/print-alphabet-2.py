n = int(input())

aph = 0

for i in range(n):

    for j in range(i):
        print("  ",end='')

    for j in range(n - i):
        print(chr(aph % 26 + 65), end=' ')
        aph += 1
    print()