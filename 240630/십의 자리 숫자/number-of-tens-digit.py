num_list = list(map(int, input().split()))
cnt_list = [0] * 10

for num in num_list:
    cnt_list[num // 10] += 1

for i in range(1, len(cnt_list)):
    print(f"{i} - {cnt_list[i]}")