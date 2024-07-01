n = int(input())
arr = list(map(int, input().split()))

max_num = 0

for i in range(n):
    for j in range(i, n):
        if(arr[i] > arr[j]):
            continue
        else:
            if(max_num < arr[j] - arr[i]):
                max_num = arr[j] - arr[i]

print(max_num)