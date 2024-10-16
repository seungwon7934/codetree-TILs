m = 0
a = []
n = int(input())
cnt = 0
for i in range(n):
    a.append(int(input()))

    if(i == 0):
        cnt += 1
    
    elif(cnt == 0 and a[i] != a[i-1]):
        cnt += 1

    elif(a[i] == a[i-1]):
        cnt += 1

    else:
        if(cnt > m):
            m = cnt
        cnt = 1

print(m)