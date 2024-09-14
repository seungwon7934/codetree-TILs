a = list(input())
b = list(input())
f = True

if(len(a) != len(b)):
    print("No")
    f = False
else:
    a.sort()
    b.sort()
    for i in range(len(a)):
        if(a[i] != b[i]):
            print("No")
            f = False
            break

if(f):
    print("Yes")