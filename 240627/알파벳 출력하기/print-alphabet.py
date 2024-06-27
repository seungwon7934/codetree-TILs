n = int(input())

aph = 65

for i in range(n):
    for j in range(i+ 1):
        print(chr(aph),end='')
        aph += 1
    print()