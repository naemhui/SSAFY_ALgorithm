def counting_charge():
    for i in range(m+1):  # 위에서 두 개 더햇자늠
        if charge[i+1] - charge[i] > k:  # 두 충전소 위치의 차 > 갈 수 있는 최대 거리
            return 0
        
    now = 0  # 현재 위치
    cnt = 0
    for i in range(1, m+2):
        if now + k < charge[i]:  # 현재 위치 + 갈 수 있는 거리 < 정류장 위치
            cnt += 1  # 충전
            now = charge[i-1]  # 충전을 해야되니까 현재 위치를 충전소 위치로
    return cnt

t = int(input())
for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    charge = [0] + list(map(int, input().split())) + [n]  # 출발 위치[0], 종점 위치[n]

    print(f'#{tc} {counting_charge()}')