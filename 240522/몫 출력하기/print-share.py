n = 1
cnt = 3
while(cnt > 0):
    n = int(input())
    if(n % 2 == 0 and cnt > 0):
        print(n//2)
        cnt -= 1