arr = input().split()

l = 0

for i in range(len(arr)):
    l += len(arr[i])

print(l)