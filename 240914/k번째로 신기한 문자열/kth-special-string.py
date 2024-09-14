n, k, t = input().split()
n = int(n)
k = int(k)

arr = list()
arr.append(t)
for _ in range(n):
    arr.append(input())

arr.sort()

print(arr[arr.index(t) + 3])