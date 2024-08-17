di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def is_valid(i, j, N, M):
    return 0<=i<N and 0<=j<M

def balloon(arr, N, M):
    max_v = 0
    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for k in range(arr[i][j]):
                for d in range(4):
                    ni = i + di[d]*(k+1)
                    nj = j + dj[d]*(k+1)

                    if is_valid(ni, nj, N, M):
                        total += arr[ni][nj]

            if total > max_v:
                max_v = total
    return max_v

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = balloon(arr, N, M)

    print(f'#{tc} {max_v}')