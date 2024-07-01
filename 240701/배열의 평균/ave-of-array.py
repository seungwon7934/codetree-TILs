arr2 = []

for _ in range(2):
    arr1 = list(map(int, input().split()))
    arr2.append(arr1)


for i in range(2):
    print(sum(arr2[i]) / len(arr2[i]), end=' ')
print()

total = 0

for i in range(4):
    col_sum = 0
    for j in range(2):
        total += arr2[j][i]
        col_sum += arr2[j][i]
    print(col_sum / len(arr2), end=' ')
print()

print(f"{total / (len(arr2[0]) * len(arr2)):.1f}")