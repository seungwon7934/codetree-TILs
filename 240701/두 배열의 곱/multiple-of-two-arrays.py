arr1 = [
    [0 for _ in range(3)]
        for _ in range(3)
]
arr2 = [
    [0 for _ in range(3)]
        for _ in range(3)
]

for i in range(3):
        arr1[i] = list(map(int, input().split()))
e = input()
for i in range(3):
        arr2[i] = list(map(int, input().split()))


for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end=' ')
    print()