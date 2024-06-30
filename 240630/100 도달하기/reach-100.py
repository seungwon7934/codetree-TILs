n = int(input())

arr = list()

arr.append(1)
arr.append(n)

print(1, n, end=' ')

m = 0
while(m < 100):
    arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])
    print(arr[len(arr) - 1], end=' ')
    m = arr[len(arr) - 1]