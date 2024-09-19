class Student:
    def __init__(self, height, weight, index):
        self.height = height
        self.weight = weight
        self.index = idx

n = int(input())

s = []
idx = 1

for _ in range(n):
    h, w = map(int, input().split())
    s.append(Student(h, w, idx))
    idx += 1

s.sort(key=lambda x:(-x.height, -x.weight, x.index))

for ss in s:
    print(ss.height, ss.weight, ss.index)