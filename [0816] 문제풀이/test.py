# def is_valid(i, N):
#     return 0<=i<N
#
# T = int(input())
# d = [1, -1]
#
# for tc in range(1, T+1):
#     N, D = map(int, input().split())
#     garden = [0]*N
#     cnt = 0
#
#     for i in range(N):
#     # while 0 not in garden:
#         if 0 not in garden:
#             # print(f'#{tc} {cnt}')
#             print(f'#{tc} {garden}')
#
#         else:
#             for j in range(2):
#                 for k in range(1, D+1):
#                     ni = i + d[j]*k
#
#                 if is_valid(ni, N) and garden[ni]==0:
#                     garden[ni] = 1


# arr = [list(input()) for _ in range(3)]
# print(arr)

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     color = [[0]*M for _ in range(N)]
#
#     print(arr)
#     print(color)

# days = 0
# N = 2
# cnt = 0
# day = [0, 1, 0, 0, 0, 0, 0]

# d = day.index(1)
# print(d)
# while cnt < N:
#     if cnt >= N:
#         print(f'# {days}')
#         break
#     else:
#         d = days % 7
#         if day[d] == 1:
#             cnt += 1
#             days += 1
#             print(cnt, days)
#         elif day[d] == 0:
#             days += 1
#             print(cnt, days)

# while cnt < N:
#     d = days % 7
#     if day[d] == 1:
#         cnt += 1
#         days += 1
#         print(cnt, days)
#     elif day[d] == 0:
#         days += 1
#         print(cnt, days)
#
#     if cnt >= N:
#         print(f'# {days}')
#         break

r, c = (0, 0)
print(r)
print(c)
print(type(r))