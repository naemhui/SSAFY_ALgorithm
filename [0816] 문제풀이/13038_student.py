'''
인덱스:  0 1 2  3  4 5  6
요일 : 일 월 화 수 목 금 토
'''

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     day = list(map(int, input().split()))

#     # cnt = 0  # 수업 들은 날 카운트, N이랑 같아지면 프린트
#     min_days = 0  # 최소 날짜

#     for start in range(7):
#         if day[start] == 1:  # 수업 있는 요일이면
#             cnt = 0
#             days = 0
#             now_day = start

#             while cnt < N:
#                 if day[now_day % 7] == 1:
#                     cnt += 1
#                 now_day += 1
#                 days += 1

#             min_days = min(min_days, days)

#     print(f'#{tc} {min_days}')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    days = list(map(int, input().split()))

    # 수업이 열리는 요일들 추출
    open_days = [i for i in range(7) if days[i] == 1]
    total = len(open_days)

    # 한 주에 수업이 열리는 요일이 부족하면 주기를 여러 번 반복해야 한다.
    min_days = -100
    for start in range(7):
        if days[start] == 1:  # 수업이 있는 날부터 시작
            cnt = 0
            now_day = start
            day = 0

            while cnt < n:
                if days[now_day % 7] == 1:
                    cnt += 1
                now_day += 1
                day += 1

