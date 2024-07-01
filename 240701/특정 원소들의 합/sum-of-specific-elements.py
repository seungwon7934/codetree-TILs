arr = []

for _ in range(4):
    arr1 = list(map(int, input().split()))
    arr.append(arr1)

total = 0

for i in range(len(arr)):
    for j in range(i+1):
        total += arr[i][j]

print(total)