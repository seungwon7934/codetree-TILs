s = list(input())

idx = ''.join(s).find('e')

if(idx != -1):
    s.pop(idx)

print(''.join(s))