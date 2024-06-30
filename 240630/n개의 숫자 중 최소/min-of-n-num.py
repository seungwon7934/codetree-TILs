n = int(input())
arr = list(map(int, input().split()))

cnt = 1
min_num = arr[0]

for num in arr:
    if (min_num == num):
        cnt += 1
    elif (min_num > num):
        min_num = num
        cnt = 1


print(min_num, cnt)