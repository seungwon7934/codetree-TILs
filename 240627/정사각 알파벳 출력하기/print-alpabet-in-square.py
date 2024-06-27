n = int(input())

a = 0

for i in range(n):
    for j in range(n):
        print(chr(a + 65),end='')
        a += 1
    print()