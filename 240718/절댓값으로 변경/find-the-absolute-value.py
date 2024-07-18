def absolute(arr):
    for num in arr:
        print(abs(num),end=' ')

n = int(input())
arr = list(map(int, input().split()))

absolute(arr[:])