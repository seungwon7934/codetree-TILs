n, k = map(int, input().split())
arr = list()

nums = map(int, input().split())

for num in nums:
    arr.append(num)

arr.sort()

print(arr[k-1])