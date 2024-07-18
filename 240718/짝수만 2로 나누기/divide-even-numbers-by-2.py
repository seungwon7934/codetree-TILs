def divide(l, arr):
    for i in range(l):
        if(arr[i] % 2 == 0):
            print(arr[i] // 2,end=' ')
        else:
            print(arr[i],end=' ')
n = int(input())
arr = list(map(int,input().split()))

divide(n, arr[:])