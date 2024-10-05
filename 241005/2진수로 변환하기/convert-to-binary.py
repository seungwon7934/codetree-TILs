n = int(input())

m = []
if(n == 0):
    m.append(0)

while(n != 0):
    r = n % 2
    m.append(r)
    n //= 2



m.reverse()

for i in m:
    print(i,end='')