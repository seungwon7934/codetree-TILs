w = 'END'

for _ in range(10):
    s = input()
    if(s == w):
        break
    else:
        print(s[::-1])