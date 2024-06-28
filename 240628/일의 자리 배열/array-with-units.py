a, b = tuple(map(int, input().split()))

arr = list()
arr.append(a)
arr.append(b)

for i in range(2, 10):
    arr.append(arr[i-1] + arr[i-2]) 

for num in arr:
    print(num % 10, end=' ')