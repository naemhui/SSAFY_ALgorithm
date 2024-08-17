'''
N X M
가로 M: 행
세로 N: 열
#->검정색(1), .->흰색(2)
? -> 검 또는 흰
'''


def is_valid(i, j, N, M):
    return 0<=i<N and 0<=j<M

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    color = [[0]*M for _ in range(N)]

    # N = 3  M = 6
    # [['#', '.', '?', '?', '?', '?'],
    # ['?', '#', '?', '?', '?', '?'],
    # ['?', '?', '?', '.', '?', '?']]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '#':
                color[i][j] = 1
            elif arr[i][j] == '.':
                color[i][j] = 2

    # 이제 빈 곳 채우기
    for i in range(N):
        for j in range(M):
            if color[i][j] == 0:
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    # 사방이 검정색이면
                    if is_valid(ni, nj, N, M) and arr[ni][nj] == 1:
                        pass
                color[i][j] = 2  # 흰색 칠하기

                    # # 사방이 흰색이면
                    # elif is_valid(ni, nj, N, M) and arr[ni][nj] == 2:
                    #     color[i][j] = 1  # 검정 칠하기
                    #
                    # # 사방이 다른 색이면
                    # else:
                    #     print(f'#{tc}', 'impossible')
                    #     break
    print(f'#{tc}', 'possible')
