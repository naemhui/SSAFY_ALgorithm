# 그냥 보면 8방향 같지만
# 사실 좌,우는 중복임
# 마찬가지로 상,하도 중복
# 남은 대각선 4방향도 선을 쭉 그어보면 중복임을 알수 있음
# 그래서 4방향만 판단해도 오목 판정이 가능함

di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]
def f(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                ni, nj = i, j  # 돌인지 확인할 위치
                while 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
                    cnt += 1
                    if cnt==5:
                        return 'YES'
                    ni += di[k]
                    nj += dj[k]
    return 'NO'  # 모든 자리 i,j에서 모든 방향 k에 대해 실패하면

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {f(N)}')