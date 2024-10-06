# 미로
def is_valid(r,c,N):
    return 0<=r<N and 0<=c<N

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(y, x):
    global result
    # 현재 위치가 목표점에 도달했거나 결과가 이미 있다면 return
    if arr[y][x] == 3 or result:
        result = 1
        return
    
    # 현재 위치를 벽으로 체크 -> 재방문하지 않도록 설정
    arr[y][x] = 1
    
    for d in range(4):
        ny = y + dr[d]
        nx = x + dc[d]
        # 반복 중 결과가 나왔다면 리턴
        if result:
            return
        # 벽이 아니거나 방문하지 않은 위치라면 이동
        if is_valid(ny,nx,N) and arr[ny][nx] != 1:
            dfs(ny, nx)

for tc in range(1, 11):
    int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0

    # (1,1)부터 탐색 시작
    dfs(1,1)
    print(f'#{tc} {result}')