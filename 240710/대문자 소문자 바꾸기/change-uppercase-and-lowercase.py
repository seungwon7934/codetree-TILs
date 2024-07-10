s = input()

for c in s:
    if(65 <= ord(c) <= 90):
        print(chr(ord(c) + 32),end='')
    else:
        print(chr(ord(c) - 32),end='')