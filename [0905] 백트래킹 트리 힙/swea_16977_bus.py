'''
최소한의 충전이 관건이므로
재귀를 돌면서 카운팅된 수 > 저장된 수 이면 재귀를 하지 않도록 설정
'''


T = int(input())
for tc in range(1, T + 1):
    N, *busstop = map(int, input().split())

    # 중복 계싼 방지 위해
    # 내가 중간에 계산할 값 저장
    DP = [99999] * N
    # DP[i] : i번까지 가는데 최소 충전 횟수
    DP[0] = 0

    # 모든 위치에서 충전해보고 이전에 계산한 적이 없으면 계산
    for i in range(1, N):
        # 위치 i까지 오는 데 최소 충전 횟수?
        # i에 오기 전 위치 j
        # j+busstop[j] >= i 이면 i에 올 수 있따
        # i까지 오는데 최소 충전 횟수 = j까지 오는 데 최소 충전 횟수 +1
        # 이전에 다른 j에서 왔던 횟수와 비교해서 최소값만 저장
        for j in range(i):
            if j + busstop[j] >= i:  # j에서 i로 이동 가능
                DP[i] = min(DP[i], DP[j]+1)
    # 반복문이 끝나면 DP의 마지막 값에 최소 충전 횟수 있따
    print(f'#{tc} {DP[N-1]-1}')