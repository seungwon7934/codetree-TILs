arr = list(map(int, input().split()))
idx = 0

for num in arr:
    if(num != 0):
        idx += 1
    else:
        break

print(sum(arr[:idx:]))