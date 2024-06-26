n = int(input())

for i in range(n * n):
    print(f"{ 9 - i % 9}",end='')
    if((i + 1) % n == 0):
        print()