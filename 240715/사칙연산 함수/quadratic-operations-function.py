def plus(a, c):
    return a + c

def minus(a, c):
    return a - c

def multiply(a, c):
    return a * c

def divide(a, c):
    return a // c

a, o, c = input().split()
a = int(a)
c = int(c)
if(o == "+"):
    print(f"{a} {o} {c} = {plus(a, c)}")
elif(o == "-"):
    print(f"{a} {o} {c} = {minus(a, c)}")
elif(o == "/"):
    print(f"{a} {o} {c} = {divide(a, c)}")
elif(o == "*"):
    print(f"{a} {o} {c} = {multiply(a, c)}")

else:
    print("False")