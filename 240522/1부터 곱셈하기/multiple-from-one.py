n = int(input())

m = 1

for i in range(1, n+1):
    m *= i
    if(m >= n):
        print(i)
        break;