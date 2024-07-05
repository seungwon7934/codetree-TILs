s = list(input())

s[1] = 'a'
s[len(s) - 2] = 'a'

s = ''.join(s)

print(s)