n = 0

while(1):
    n = int(input())
    if(1 <= n <= 4):
        if(n == 1):
            print("John")
        elif(n == 2):
            print("Tom")
        elif(n == 3):
            print("Paul")
        else:
            print("Sam")
    else:
        print("Vacancy")
        break