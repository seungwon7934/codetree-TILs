n, m = map(int, input().split())
arr = list(map(int, input().split()))
total = 0

while(m != 0):
    total += arr[m-1]
    if(m % 2 == 0):
        m //= 2
    else:
        m -= 1

print(total)