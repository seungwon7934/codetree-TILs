a, b = map(int, input().split())

for i in range(a):
    for j in range(b):
        print(f"{(i + 1) * (j+1)} ",end='')
    print()