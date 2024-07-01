arr = list(map(int, input().split()))

min_num = arr[0]
max_num = arr[0]

for num in arr:
    if(num == 999 or num == -999):
        break

    if(min_num > num):
        min_num = num
    
    if(max_num < num):
        max_num = num

print(max_num, min_num)