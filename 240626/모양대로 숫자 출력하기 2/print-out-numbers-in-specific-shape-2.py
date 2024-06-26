n = int(input())

for i in range(n * n):
    print(f"{(i * 2) % 8 + 2} ",end='')
    if((i + 1) % n == 0):
        print()