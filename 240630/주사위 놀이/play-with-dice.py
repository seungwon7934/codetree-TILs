num_list = list(map(int, input().split()))

cnt_list = [0] * 6

for num in num_list:
    cnt_list[num - 1] += 1

for i in range(len(cnt_list)):
    print(f"{i + 1} - {cnt_list[i]}")