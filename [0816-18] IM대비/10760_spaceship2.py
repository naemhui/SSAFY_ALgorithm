'''
사진 가능 : 착륙지점보다 높이 낮은 구역
-> 최적의 착륙 장소 정할 수 있음
-> 예비 후보지: 사진 4방향 이상 가능
-> 예비 후보지 개수 출력
'''

def is_valid(r, c, N, M):
    return 0<=r<N and 0<=c<M

## 상1 상2 상3 하1 하2 하3 좌 우
dr = [-1, -1, -1, 1, 1, 1, 0, 0]
dc = [-1, 0, 1, -1, 0, 1, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total = 0  # 예비 후보지 개수

    for r in range(N):
        for c in range(M):
            cnt = 0  # 낮은 구역 개수 카운트
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_valid(nr,nc,N,M):
                    if arr[r][c] > arr[nr][nc]:
                        cnt += 1
            if cnt >= 4:
                total += 1
    print(f'#{tc} {total}')