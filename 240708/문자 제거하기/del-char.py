s = list(input())

while(len(s) != 1):
    idx = int(input())
    if(len(s) <= idx):
        s.pop(len(s) - 1)
    else:
        s.pop(idx)
    print(''.join(s))