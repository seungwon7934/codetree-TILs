class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

w = []

for _ in range(n):
    arr = input().split()
    w.append(Weather(arr[0], arr[1], arr[2]))

w.sort(key = lambda x:x.date)

for i in range(n):
    d = w[i]
    if(d.weather == "Rain"):
        print(d.date, d.day, d.weather)
        break