n = int(input())

for i in range(1, n+1):
    if(i == 100):
        print(i)
    elif(i >= 10):
        a = i/10;
        b = i%10;
        if(a == 3 or b == 3):
            print(0, end=' ')
        else:
            print(i, end=' ')
    else:
        if(i % 3 == 0):
            print(0, end=' ')
        else:
            print(i, end=' ')