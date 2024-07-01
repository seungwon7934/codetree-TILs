n = int(input())
arr = list(map(int, input().split()))

min_minus = 999999

for i in range(n):
    for j in range(i+1, n):
        if(abs(arr[i] - arr[j]) < min_minus):
            min_minus = abs(arr[i] - arr[j])

print(min_minus)