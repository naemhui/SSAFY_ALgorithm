di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  # 최대 꽃가루 합계
    for i in range(N):  # 터트려볼 풍선의 위치  NxM 크기의 게임판
        for j in range(M):
            cnt = arr[i][j]  # 터트린 풍선의 꽃가루 수
            # 주변 풍선의 꽃가루
            for k in range(4):  # 확인할 방향. 주변 풍선의 인덱스 ni, nj
                for l in range(1, arr[i][j] + 1):  # (i,j)에 있던 꽃가루 개수만큼 사방으로 퍼져나감
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]  # 주변의 풍선에서 나오는 꽃가루 추가
            # 꽃가루를 최대값과 비교
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')