n = int(input())
arr = list(map(int, input().split()))

start_idx = len(arr)

for i in range(n):
    max_num = arr[0]
    max_left_idx = 1

    for j in range(start_idx):
        
        if(max_num < arr[j]):
            max_num = arr[j]
            max_left_idx = j + 1

    print(max_left_idx, end=' ')
    start_idx = max_left_idx - 1

    if(max_left_idx == 1):
        break