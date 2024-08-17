T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # cq = [0] * N
    front = rear = 0

    cq = list(map(int, input().split()))

    for _ in range(M):
        front = (front + 1) % N

    result = cq[front]
    print(f'#{tc} {result}')