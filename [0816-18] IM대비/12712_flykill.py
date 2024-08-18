def is_valid(r,c,N):
    return 0<=r<N and 0<=c<N

# 상하좌우
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# 2, 1, 3, 4사분면
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_die = 0

    for r in range(N):
        for c in range(N):
            
            die = arr[r][c]
            # 1. + 형태
            for d in range(4):
                for m in range(1, M):
                    nr = r + di[d]*m
                    nc = c + dj[d]*m
                    if is_valid(nr,nc,N):
                        die += arr[nr][nc]
            if die > max_die:
                max_die = die
            
            die = arr[r][c]
            # 2. x 형태
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr[d]*m
                    nc = c + dc[d]*m
                    if is_valid(nr,nc,N):
                        die += arr[nr][nc]

            if die > max_die:
                max_die = die

    print(f'#{tc} {max_die}')