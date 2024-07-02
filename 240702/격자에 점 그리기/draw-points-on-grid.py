n, m = map(int, input().split())

arr = [
    [0 for _ in range(n)]
        for _ in range(n)
]

for i in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = i + 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()