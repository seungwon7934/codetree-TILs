s = input()

for i in range(len(s)):
    if(47 < ord(s[i]) < 58 or 96 < ord(s[i]) < 123):
        print(s[i],end='')
    elif(64 < ord(s[i]) < 91):
        print(chr(ord(s[i]) + 32),end='')