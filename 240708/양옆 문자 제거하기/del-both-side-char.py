s = list(input())

s = s[:2] + s[3:len(s) - 2] + s[len(s) - 1:]

s = ''.join(s)

print(s)