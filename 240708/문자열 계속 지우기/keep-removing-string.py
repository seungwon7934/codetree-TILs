a = list(input())
b = list(input())

isTrue = False

while(isTrue != True):
    i = 0
    for i in range(len(a) - 1):
        if(a[i:i+2] == b):
            a.pop(i)
            a.pop(i)
            break
    
    if(''.join(a).find(''.join(b)) == -1):
        isTrue = True

print(''.join(a))