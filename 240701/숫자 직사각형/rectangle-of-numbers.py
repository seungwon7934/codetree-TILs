n, m = map(int, input().split())

arr = [
    [j * m + i + 1 for i in range(m)]
    for j in range(n)
]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()