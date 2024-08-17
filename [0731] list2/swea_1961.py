def turn(arr, n):
    # dr = [0, 1, 0, -1] 
    # dc = [1, 0, -1, 0]

    arr_90 = [[0]*n for _ in range(n)]
    arr_180 = [[0]*n for _ in range(n)]
    arr_270 = [[0]*n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            arr_90[c][n-1-r] = arr[r][c]  # 90도
            arr_180[n-1-r][n-1-c] = arr[r][c]  # 180도
            arr_270[n-1-c][r] = arr[r][c]  # 270도

    return arr_90, arr_180, arr_270

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # arr = [list(map(int, input().split())) for _ in range(n)]
    arr_90, arr_180, arr_270 = turn(arr, n)

    print(f'#{tc}')
    for i in range(n):
        print(''.join(map(str, arr_90[i])), end=' ')
        print(''.join(map(str, arr_180[i])), end=' ')
        print(''.join(map(str, arr_270[i])), end=' ')
        print(" ")
