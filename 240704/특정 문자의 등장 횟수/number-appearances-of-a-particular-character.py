s = input()

c1 = 0
c2 = 0


for i in range(len(s) - 1):
    if(s[i:i+2] == 'ee'):
        c1 += 1
    if(s[i:i+2] == 'eb'):
        c2 += 1

print(c1, c2)