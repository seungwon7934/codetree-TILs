n = int(input())
arr = list(map(int, input().split()))

cnt = 1
min_num = arr[0]

for i in range(1, len(arr)):
    if (min_num == arr[i]):
        cnt += 1
    elif (min_num > arr[i]):
        min_num = arr[i]
        cnt = 1


print(min_num, cnt)