arr = list(map(int, input().split()))

max_num = arr[0]

for num in arr:
    if(max_num < num):
        max_num = num

print(max_num)

# print(max(arr))