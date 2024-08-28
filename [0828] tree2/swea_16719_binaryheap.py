# 5177. 이진 힙
def insert(num):
    global last
    last += 1
    h[last] = num
    c = last  # 자식 노드와 부모 노드 비교를 위해
    p = c//2

    # 계속 올라가면서 부모 자식 비교
    while p >= 1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드 수
    arr = list(map(int, input().split()))  # 입력 값 리스트
    last = 0
    h = [0] * (N+1)
    for d in arr:
        insert(d)

    sumV = 0
    # 현재 last는 N
    while last >= 1:
        last //= 2
        sumV += h[last]  # 조상 노드를 더해줌

    print(f'#{tc} {sumV}')