n = int(input())


arr = [
    [n * i + j for i in range(n)]
        for j in range(1, n + 1)
]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()