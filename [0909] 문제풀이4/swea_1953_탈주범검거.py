# '''
# 한 시간 후 맨홀로 들어감
# 지도, 맨홀 위치, 경과시간 주어짐
# N,M RC L
# N줄 주어짐
# '''
# # 상 하 좌 우
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# # 1: for d in range(4)
# # 2: for d in [0, 1]
# # 3: for d in [2, 3]
# # 4: for d in [0, 3]
# # 5: for d in [1, 3]
# # 6: for d in [1, 2]
# # 7: for d in [0, 2]
#
# def is_valid(r,c,N,M):
#     return 0<=r<N and 0<=c<M
#
# direction = [[], [0,1,2,3], [0,1], [2,3], [0,3], [1,3], [1,2], [0,2]]
# # arr[R][C] 는 1~7 중 하나. 즉, direction의 인덱스
#
# def where(r,c, time):
#     global cnt
#     if time == L:
#         for i in range(N):
#             for j in range(M):
#                 if candidates[i][j] >= 1:
#                     cnt += 1
#         return cnt
#
#     for d in direction[arr[R][C]]:
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if is_valid(nr,nc,N,M):
#             candidates[nr][nc] = 1
#
#         where(nr,nc, time+1)
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, R, C, L = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     candidates = [[0] * M for _ in range(N)]
#     # 시작점 : (R, C)
#     candidates[R][C] = 1
#     cnt = 0
#     result = where(R,C,1)
#
#     print(f'#{tc} {result}')
from collections import deque

def is_valid(i,j,N,M):
    return 0<=i<N and 0<=j<M

def bfs(sti, stj):
    global cnt
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((sti, stj, 1))
    visited[sti][stj] = 1

    while q:
        # 종료 조건
        i, j, time = q.popleft()
        if time == L:
            return

        for d1 in direction[arr[i][j]]:
            ni, nj = i + dr[d1], j + dc[d1]

            if is_valid(ni,nj,N,M) and visited[ni][nj] == 0 and arr[ni][nj] != 0:

                for d2 in direction[arr[ni][nj]]:
                    newi, newj = ni+dr[d2], nj+dc[d2]

                    if newi == i and newj == j:
                        q.append((ni, nj, time + 1))
                        visited[ni][nj] = 1
                        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    direction = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

    cnt = 1
    bfs(R, C)
    print(f'#{tc} {cnt}')