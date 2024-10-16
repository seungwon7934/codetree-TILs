n, m, k = map(int, input().split())
isPaid = False

s = {}

for _ in range(m):
    idx = int(input())

    if(idx not in s):
        s[idx] = 1

    else:
        s[idx] += 1

    for i in s:
        if(s[i] == k):
            print(i)
            isPaid = True
    
    if(isPaid == True):
        break

if(isPaid == False):
    print(-1)