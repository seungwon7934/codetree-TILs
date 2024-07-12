def num_rect(n):
    for i in range(n**2):
        if(i != 0 and i % n == 0):
            print()
        print(i % 9 + 1,end=' ')

n = int(input())

num_rect(n)