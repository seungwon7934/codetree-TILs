n = int(input())

for i in range(n):
    for j in range(n):
        if(i <= j):
            print(f"{n - j} ",end='')
        else:
            print("  ",end='')
    print()