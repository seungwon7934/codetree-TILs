def sign(n):
    if(n > 0):
        return 1
    else:
        return -1


n = int(input())
a = []
l = 0
cnt = 0

for i in range(0, n):
    a.append(int(input()))

    if(i == 0):
        cnt += 1
    
    elif(sign(a[i]) == sign(a[i-1])):
        cnt += 1
    
    else:
        cnt = 1

    if(cnt > l):
        l = cnt
    
print(l)