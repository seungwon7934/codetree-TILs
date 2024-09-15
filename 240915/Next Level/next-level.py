class user:
    def __init__(self, uid='codetree', level=10):
        self.uid = uid
        self.level = level

i, l = input().split()

u1 = user()
u2 = user(i, l)

print("user " + u1.uid + " lv " + str(u1.level))
print("user " + u2.uid + " lv " + str(u2.level))