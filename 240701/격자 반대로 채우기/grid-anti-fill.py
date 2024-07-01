n = int(input())

arr = [
    [0 for _ in range(n)]
        for _ in range(n)
]

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if((i - n) % 2 != 0):
            arr[j][i] = n * n - n * (i + 1) + n - j
        else:
            arr[j][i] = n * n - n * (i + 1) + j + 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()