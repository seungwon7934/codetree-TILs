N, k, p, T = map(int, input().split())

# n: 개발자 수
# k: 감염시킬 수 있는 악수 횟수
# p: 처음 질병에 걸린 개발자의 번호
# t: 악수 진행 횟수

dev_meeting_list = {}  # 개발자 만남 리스트
dev_infection_count_list = [0] * (N + 1)  # 개발자 감염 횟수
dev_infection_list = [0] * (N + 1) # 감염된 개발자 리스트

dev_infection_count_list[p] = 2
dev_infection_list[p] = 1

for _ in range(T):

    t, x, y = map(int, input().split())

    if(t not in dev_meeting_list):
        dev_meeting_list[t] = (x,y)

for i in range(250):
    if(i in dev_meeting_list):
        x, y = dev_meeting_list[i]

        if(dev_infection_count_list[x] > 0 and dev_infection_count_list[y] == 0):
            dev_infection_count_list[x] -= 1
            dev_infection_count_list[y] = 2
            dev_infection_list[y] = 1

        
        elif(dev_infection_count_list[y] > 0 and dev_infection_count_list[x] == 0):
            dev_infection_count_list[y] -= 1
            dev_infection_count_list[x] = 2
            dev_infection_list[x] = 1
        
        elif(dev_infection_count_list[x] > 0 and dev_infection_count_list[y] > 0):
            dev_infection_count_list[x] -= 1
            dev_infection_count_list[y] -= 1

for i in range(1, len(dev_infection_list)):
    print(dev_infection_list[i], end='')