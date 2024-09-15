class info:
    def __init__(self, grade="N", score=0):
        self.grade = grade
        self.score = score

students = [
    tuple(input().split())
    for _ in range(5)
]

idx = 0
sc = 100
for i in range(len(students)):
    _, s = students[i]
    if(sc < int(s)):
        sc = int(s)
        idx = i

g, s = students[idx]

print(g, s)