n = int(input())
arr = list(map(int, input().split()))



for i in range(n):
    for j in range(i):
        temp = 0
        if(arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for num in arr:
    print(num, end=' ')

print()

for i in range(n):
    for j in range(i):
        temp = 0
        if(arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for num in arr:
    print(num, end=' ')