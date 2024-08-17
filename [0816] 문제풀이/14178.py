'''
좌표 x -> x-D ... x+D까지
'''

def is_valid(i, N):
    return 0<=i<N

T = int(input())
d = [1, -1]

for tc in range(1, T+1):
    N, D = map(int, input().split())
    garden = [0]*N
    cnt = 0

    for i in range(D, N, 2 * D + 1):

        if 0 not in garden:
            # print(f'#{tc} {cnt}')
            break

        else:

            for k in range(0, D + 1):
                for j in range(2):
                    ni = i + d[j] * k

                    if is_valid(ni, N) and garden[ni] == 0:
                        garden[ni] = 1
            cnt += 1
            # print(garden, cnt)
    if 0 in garden:
        cnt += 1
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc} {cnt}')





    # for i in range(D, N, 2*D+1):
    #
    #     if 0 not in garden:
    #         print(garden, cnt)
    #         break
    #
    #     else:
    #
    #         for k in range(0, D+1):
    #             for j in range(2):
    #                 ni = i + d[j]*k
    #
    #                 if is_valid(ni, N) and garden[ni]==0:
    #                     garden[ni] = 1
    #         cnt += 1
    #         print(garden, cnt)
    # if 0 in garden:
    #     cnt += 1
    #     print(garden, cnt)






                # if 0 not in garden:
                #     print(f'#{tc} {cnt}')
                #     break



# def (arr, N, M):
#     max_v = 0
#     for i in range(N):
#             for k in range(arr[i]):
#                 for d in range(4):
#                     ni = i + di[d]*(k+1)
#                     nj = j + dj[d]*(k+1)
#
#                     if is_valid(ni, nj, N, M):
#                         total += arr[ni][nj]
#
#             if total > max_v:
#                 max_v = total
#     return max_v
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = balloon(arr, N, M)
#
#     print(f'#{tc} {max_v}')