cnt_list = [0] * 10

n = int(input())
arr = list(map(int, input().split()))

for num in arr:
    cnt_list[num] += 1

for i in range(1, 10):
    print(cnt_list[i])