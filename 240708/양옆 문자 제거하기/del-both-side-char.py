s = list(input())

s = s[:1] + s[2:len(s) - 2] + s[len(s) - 1:]

s = ''.join(s)

print(s)