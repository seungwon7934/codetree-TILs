n = int(input())

i = 1
for cnt in range(1, n * n + 1):
    if(((cnt - 1) // n) % 2 == 0):
        print(f"{i} ", end='')
    else:
        i += 1
        print(f"{i} ", end='')

    if (cnt % n == 0):
        print()

    i += 1