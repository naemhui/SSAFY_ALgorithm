def is_valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def max_ballon(arr, n, m):
    max_v = 0

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            total = arr[i][j]
            for k in range(arr[i][j]):
                for d in range(4):
                    ni = i + di[d]*(k+1)
                    nj = j + dj[d]*(k+1)
                    if is_valid(ni, nj, n, m):
                        total += arr[ni][nj]

            if total > max_v:
                max_v = total
    return max_v

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = max_ballon(arr, n, m)

    print(f'#{tc} {max_v}')