n = int(input())

for i in range(1, n * n  + 1):
    if(((i - 1) // n) % 2 == 0):
        print(f"{i} ", end='')
    else:
        print(f"{((i - 1) // n + 1) * n - (i - 1) % n} ", end='')
    
    if((i) % n == 0):
        print()