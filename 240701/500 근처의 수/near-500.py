arr = list(map(int, input().split()))

five_over_min = arr[0]
five_under_max = arr[0]

for num in arr:
    if(num > 500):
        if(five_over_min < 500):
            five_over_min = num
        if(five_over_min > num):
            five_over_min = num
    else:
        if(five_under_max < num):
            five_under_max = num

print(five_under_max, five_over_min)