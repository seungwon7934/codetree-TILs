#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

start = d1
end = d2 + 1

for i in range(m1):
    start += num_of_days[i]

for i in range(m2):
    end += num_of_days[i]

print(end - start)