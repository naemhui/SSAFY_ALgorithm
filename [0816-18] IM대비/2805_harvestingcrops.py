T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 가장 가운데 인덱스 : arr[N//2][N//2]
    total = 0

    # i = 0, j = [3] 3
    # i = 1, j = [2:5] 2 3 4
    # i = 2, j = [1:6] 1 2 3 4 5
    # i = 3, j = [:] 0 1 2 3 4 5 6 7

    for r in range(N):
        # 중심 인덱스와 떨어져있는 만큼 앞뒤 빼기
        idx = abs(N//2-r)  # 떨어진 정도: abs(N//2 - r)
        for c in range(idx, N-idx):
            total += arr[r][c]
            # print(arr[r][c])

    print(f'#{tc} {total}')