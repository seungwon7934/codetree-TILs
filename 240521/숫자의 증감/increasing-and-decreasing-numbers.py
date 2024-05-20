arr = input().split()

c = arr[0]
n = int(arr[1])

if(c=='A'):
    i = 1
    while(i <= n):
        print(i, end=' ')
        i += 1
else:
    while(n > 0):
        print(n, end=" ")
        n -= 1