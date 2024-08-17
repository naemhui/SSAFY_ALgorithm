from collections import deque

def bfs(i, j, N, maze):
    visited = [[0]*N for _ in range(N)]  # 방문 기록
    q = deque()
    q.append((i,j))  # 시작점 -> q에 추가
    visited[i][j] = 1  # 시작점 -> 방문 표시

    # BFS 탐색
    while q:  # q에 탐색할 위치가 있는 동안
        ti, tj = q.popleft()  # 현재 위치 꺼내고 현재 위치로 이동

        # 도착점에 도달
        if maze[ti][tj] == 3:
            return 1
        
        # 상하좌우 이동
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0<wi<N and 0<=wj<N and maze[wi][wj] != 1 and not visited[wi][wj]:
                q.append((wi, wj))  # 인접 칸 큐에 추가
                visited[wi][wj] = 1  # 방문 표시
    
    # 큐가 비었는데도?
    return 0  # 도착점 도달 X

# 출발점 찾는 함수
def find_start(N, maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
            
for _ in range(10):
    N = 16
    tc = input()  # tc 번호
    maze = [list(map(int, input().strip())) for _ in range(N)]
    sti, stj = find_start(N, maze)
    ans = bfs(sti, stj, N, maze)
    print(f'#{tc} {ans}')        