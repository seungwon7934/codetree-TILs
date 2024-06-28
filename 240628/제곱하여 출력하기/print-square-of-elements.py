n = int(input())

arr = list(map(int, input().split()))

squared_arr = [num ** 2 for num in arr]

for num in squared_arr:
    print(num, end=' ')