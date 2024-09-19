class Student:
    def __init__(self, name, one, two, three):
        self.name = name
        self.one = one
        self.two = two
        self.three = three

n = int(input())

s = []

for _ in range(n):
    arr = input().split()

    s.append(Student(arr[0], int(arr[1]), int(arr[2]), int(arr[3])))

s.sort(key = lambda x:(x.one + x.two + x.three))

for ss in s:
    print(ss.name, ss.one, ss.two, ss.three)