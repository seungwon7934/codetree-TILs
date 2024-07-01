n, m = map(int, input().split())

arr1 = [
    [0 for _ in range(n)]
        for _ in range(m)
]

arr2 = [
    [0 for _ in range(n)]
        for _ in range(m)
]


for i in range(n):
    arr1[i] = list(map(int, input().split()))

for i in range(n):
    arr2[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if(arr1[i][j] == arr2[i][j]):
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()