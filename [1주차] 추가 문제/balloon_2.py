def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def max_ballon(arr, n, m):
    max_v = 0
    # 방향 벡터
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            total = arr[i][j]
            # 4방향 탐색
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if is_valid(ni, nj, n, m):
                    total += arr[ni][nj]
            # 최대값 갱신
            if total > max_v:
                max_v = total
    return max_v

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = max_ballon(arr, n, m)

    print(f'#{tc} {max_v}')



# def is_valid(i, j):
#     return 0 <= i < n and 0 <= j < m

# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]  

# T = int(input())

# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split()) for _ in range(n))]

#     max_v = 0

#     for i in range(n):
#         for j in range(m):
#             now = arr[i][j]
#             for d in range(4):
#                 ni = i +di[d]
#                 nj = j +dj[d]

#                 if is_valid(ni, nj):
#                     now += arr[ni][nj]
#             if now > max_v:
#                 now = max_v
    
#     print(f'#{tc} {max_v}')