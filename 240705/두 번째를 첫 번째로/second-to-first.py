s = list(input())

s1 = s[:]

for i in range(len(s)):
    if(s[i] == s1[1]):
        s[i] = s[0]
print(''.join(s))