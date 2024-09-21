class N:
    def __init__(self, num, index):
        self.num = num
        self.index = index

n = int(input())

n1 = []
n2 = []
idx = 1
arr = input().split()

for m in arr:
    n1.append(N(int(m), idx))
    n2.append(N(int(m), idx))
    idx += 1



n2.sort(key=lambda x:x.num)

for i in range(n):
    p = n1[i]
    for j in range(n):
        q = n2[j]
        if(p.num == q.num and p.index == q.index):
            print(j + 1, end=' ')