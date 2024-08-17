def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j  # 미로의 시작 위치 반환
    return -1, -1  # 내가 잘못 찾았군~ 하는 디버깅 목적(근데 이 문제에서는 그럴 일 X)


# 방법1) 재귀를 이용한 DFS
def dfs2(i, j, N):
    visited[i][j] = 1  # 들어갈 수 있는 칸에 들어가게 되면 1
    if maze[i][j] == 3:  # 도착하면 return 1
        return 1
    else:
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:  # 상하좌우
            ni, nj = i+di, j+dj
            # if 벽이 아니고                                 방문하지 않은 위치라면
            if 0<=ni<N and 0 <=nj<N and maze[ni][nj]!=1 and visited[ni][nj] == 0:  # 유망한 곳에 도달
                if dfs2(ni, nj, N):  # 찾았다면 다른 거 보지 말고
                    return 1  # 리턴 바로 해
        return 0

# 방법2) 스택을 이용한 DFS
def dfs1(sti, stj, N, maze):
    stack = []
    visited = [[0]*N for _ in range(N)]
    stack.append((sti, stj))
    visited[sti][stj] = 1

    while stack:
        i, j = stack.pop()  # 현재 위치 꺼냄

        # 도착점 도달 여부
        if maze[i][j] == 3:
            return 1  # 미로 탐색 완료!
        
        # 완료되지 않았다면 상하좌우 탐색
        for di, dj in [(0,1), (1,0),(0,-1),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] !=1 and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1
    # 도착점 못찾았으면
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 출발위치 찾기
    sti, stj = fstart(N)

####### 하단의 두 개 중 하나만 출력
    # 방법1) 미로 탐색 (재귀 사용)
    visited = [[0]*N for _ in range(N)]
    ans = dfs2(sti, stj, N)
    print(f'#{tc} {ans}')

    # 방법2) 미로 탐색 (stack 사용)
    ans = dfs1(sti, stj, N, maze)
    print(f'#{tc} {ans}')