N = 10
# N개의 원소가 있고 집합을 만드려고 한다.
p = [i for i in range(N)]
# p[i] == i가 가리키고 있는 사람 번호이지
# p[i] 는 i가 속한 집합의 대표가 아!!!!님!!!!!XXXXXXXX. 대표인 경우도 있음

# 연산의 최적화를 위해서 트리의 높이를 관리하는 rank 배열
rank = [1] * N

# x가 속한 집합의 대표를 찾는 연산
def find(x):
    # 집합의 대표가 되는 조건?
    # 부모를 가리키는 화살표가 자기 자신을 향할 때 : 그 친구가 대표
    if p[x] != x:
        # x가 자기 자신을 가리키고 있지 않으면 대표를 계속 찾아
        # 경로 압축 (바로 대표를 가리키도록)
        p[x] = find(p[x])

    # 자기 자신을 가리키고 있으면 재귀 중단하고 p[x] 리턴
    return p[x]

# x가 속한 집합과 y가 속한 집합을 합치는 연산
# 집합을 합친다 => 두 집합의 대표를 같게 한다 / 같은 말.
def union(x,y):
    # x가 속한 집합의 대표
    rootX = find(x)
    # y가 속한 집합의 대표
    rootY = find(y)

    # 두 집합의 대표가 다를 때만 합치자
    if rootX != rootY:
        # 두 집합의 높이를 비교해서 작은 쪽을 큰 쪽에 붙이자
        if rank[rootX] > rank[rootY]:
            p[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            p[rootX] = rootY
        else:
            # 두 집합의 높이가 같을 때는 한쪽에 다른 쪽을 붙이고
            # 붙인 쪽 높이+1
            # y를 x에 붙인다고 치면
            p[rootY] = rootX
            # 높이가 증가해야 하는 쪽은 x이므로
            rank[rootX] += 1