m = 0

def f(n):
    global m
    global arr
    if(n == -1):
        return
    if(m < arr[n-1]):
        m = arr[n-1]
    f(n-1)


n = int(input())
arr = list(map(int, input().split()))
f(n)
print(m)