# 상, 하, 좌, 우 방향 설정
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 유효한 인덱스인지 확인하는 함수
def is_valid(i, j, N, M):
    return 0 <= i < N and 0 <= j < M

# 마지막 check 하는 함수
def check(arr, N, M):
    for i in range(N):
        for j in range(M):
            # 1. color 배열에 0이 있다면 impossible
            if arr[i][j] == 0:
                return 'impossible'
            # 2. 인접한 두 컬러가 같으면 impossible
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if is_valid(ni, nj, N, M) and arr[i][j] == arr[ni][nj]:
                    return 'impossible'
    return 'possible'

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    color = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '#':
                color[i][j] = 1
            elif arr[i][j] == '.':
                color[i][j] = 2

    # 색상 채우기
    for i in range(N):
        for j in range(M):
            if color[i][j] == 0:
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if is_valid(ni,nj,N,M) and color[ni][nj] != 0:
                        # 인접한 칸의 색상에 따라 반대 색상 설정
                        color[i][j] = 3 - color[ni][nj]
                        break
                    else:
                        # 인접한 칸에 색상이 지정된 게 없다면 임의로 1로 설정
                        color[i][j] = 1

    # 출력
    result = check(color, N, M)
    print(f'#{tc} {result}')