def is_valid(i,j,N):
    return 0<=i<N and 0<=j<N

def omok(arr, N):
    for i in range(N):
        for j in range(N):

            if arr[i][j] == 'o':
                for d in range(4):
                    cnt = 1
                    for k in range(1, 5):
                        ni = i + di[d]*k
                        nj = j + dj[d]*k
                    
                        if is_valid(ni,nj,N) and arr[ni][nj] == 'o':
                            cnt += 1

                    if cnt == 5:
                        print(f'#{tc} YES')
                        return
    print(f'#{tc} NO')
    return


# 가로 세로 우하향 좌상향
di = [0, 1, 1, 1]
dj = [1, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    omok(arr, N)