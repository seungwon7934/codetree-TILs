n = int(input())

arr = list(map(int, input().split()))

idx_list = [0] * 1001

for num in arr:
    idx_list[num] += 1

for i in range(len(idx_list)):
    if(idx_list[i] >= 2):
        idx_list[i] == -1

idx = 0
max_num = idx_list[0]

for i in range(len(idx_list)):
    if(idx_list[i] == 1):
        idx = i


if (idx != 0):
    print(idx)
else:
    print(-1)