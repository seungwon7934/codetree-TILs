m = 0
a = []
n = int(input())
cnt = 0
for i in range(n):
    a.append(int(input()))
    if(i == 0 or a[i] == a[i-1]):
        cnt += 1
    
        if(cnt > m):
            m = cnt + 1
    else:
        cnt = 0

print(m)