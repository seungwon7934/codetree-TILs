class m:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

c, p, t = input().split()

n = m(c, p, t)

print("secret code : " + n.code)
print("meeting point : " + n.point)
print("time : " + n.time)