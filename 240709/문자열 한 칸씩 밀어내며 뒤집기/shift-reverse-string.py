arr = input().split()
s = str(arr[0])
for _ in range(int(arr[1])):
    n = int(input())
    if(n == 1):
        s = s[1:] + s[0]
        print(s)
    elif(n == 2):
        s = s[-1] + s[:-1]
        print(s)
    else:
        s = s[len(s)-1::-1]
        print(s)