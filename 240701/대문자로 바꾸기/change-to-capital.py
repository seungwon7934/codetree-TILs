arr2 = []

for _ in range(5):
    arr1 = list(input().split())
    arr2.append(arr1)

for i in range(5):
    for j in range(3):
        print(chr(ord(arr2[i][j]) - 32), end=' ')
    print()