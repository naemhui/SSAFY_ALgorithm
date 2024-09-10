def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    # x와 y의 대표를 찾음
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            p[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            p[rootX] = rootY
        else:
            p[rootY] = rootX
            rank[rootX] += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 사람 수
    p = list(range(N + 1))
    rank = [1] * (N + 1)

    for _ in range(M):
        fst, snd = map(int, input().split())
        union(fst, snd)

    result = [find(i) for i in range(1, N + 1)]

    # 대표자 집합의 수 계산
    print(f'#{tc} {len(set(result))}')