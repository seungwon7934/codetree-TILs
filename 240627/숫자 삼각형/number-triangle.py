n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(f"{j + 1} ", end='')
    print()