n = int(input())
l = 0
temp = 0
a = []


for i in range(n):
    a.append(int(input()))

    if(i == 0):
        temp += 1
    
    elif(a[i] > a[i-1]):
        temp += 1
    
    else:
        temp = 1
    
    if(temp > l):
        l = temp

print(l)