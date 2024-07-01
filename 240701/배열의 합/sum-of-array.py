arr2 = []

for _ in range(4):
    arr1 = list(map(int, input().split()))
    arr2.append(arr1)

for i in range(4):
    print(sum(arr2[i]))