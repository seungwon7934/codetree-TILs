n = int(input())

nums = map(int, input().split())
nums = list(nums)
arr = list()

for i in range(n):
    arr.append(nums[i])
    if(i % 2 == 0):
        arr.sort()
        print(arr[len(arr) // 2], end=' ')