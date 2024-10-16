n, t = map(int, input().split())
l = 0
temp = 0

a = input().split()


for i in range(n):

    if(int(a[i]) > t):
        temp += 1
    
    else:
        temp = 0
    
    if(temp > l):
        l = temp


print(l)