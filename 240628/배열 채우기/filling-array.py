arr = list(map(int, input().split()))

r_arr = list()

for i in range(len(arr)):
    if(arr[i] != 0):
        r_arr.append(arr[i])
    else:
        break

for i in range(len(r_arr)):
    print(r_arr[len(r_arr) - 1 - i], end=' ')