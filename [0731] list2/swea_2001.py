dr = [0, 0, 1, 1]
dc = [0, 1, 1, 0]

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]


def bug(arr, n, m):
    r, c = 0, 0  # 초기 위치
    sum_die = []

    for r in range(n):
        for c in range(n):
            
            die = []  # 죽은 파리 모음
            # max_die = 0  # 죽은 최대 파리 수

            for d in range(4):  # 파리채에 들어갈 값들
                nr = r + dr[d]
                nc = c + dc[d]

                if is_valid(nr, nc):  # 값이 유효하면
                    die.append(arr[nr][nc])
                    
                    if len(die) == m*m:  # 모든 값이 유효하면
                        sum_die.append(sum(die)) # 죽은 파리의 합을 list에 담음
