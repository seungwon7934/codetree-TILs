n = int(input())
arr = map(int, input().split())
arr = list(arr)
arr.sort()
m = 0
for i in range(len(arr)//2):
    if(m < arr[i] + arr[len(arr) - 1 - i]):
        m = arr[i] + arr[len(arr) - 1 - i]

print(m)