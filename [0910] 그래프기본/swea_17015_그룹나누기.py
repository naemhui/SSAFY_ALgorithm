
# x가 속한 집합의 대표를 찾는 연산
def find(x):
    # 집합의 대표를 찾기 위한 재귀 호출
    # x가 자기 자신을 가리키고 있지 않으면 대표를 계속 찾아야 함
    if p[x] != x:
        # 경로 압축 (x가 직접 대표를 가리키도록 함)
        p[x] = find(p[x])
    # 자기 자신을 가리키고 있으면 대표를 반환
    return p[x]

# x가 속한 집합과 y가 속한 집합을 합치는 연산
def union(x, y):
    # x와 y의 대표를 찾음
    rootX = find(x)
    rootY = find(y)

    # 두 집합의 대표가 다르면 합쳐야 함
    if rootX != rootY:
        # 두 집합의 높이를 비교하여 작은 쪽을 큰 쪽에 붙임
        if rank[rootX] > rank[rootY]:
            p[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            p[rootX] = rootY
        else:
            # 두 집합의 높이가 같을 때는 한 쪽의 대표를 다른 쪽에 붙이고
            # 붙인 쪽의 높이를 증가시킴
            p[rootY] = rootX
            rank[rootX] += 1

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 학생 수, M: 신청서 수
    lst = list(map(int, input().split()))  # M개의 신청서 데이터

    # 부모 정보와 트리의 높이를 관리하는 배열 초기화
    p = list(range(N + 1))  # 1부터 N까지 인덱스 사용
    rank = [1] * (N + 1)    # 트리의 높이 초기화 (모든 원소의 높이는 1)

    for i in range(M):
        fst = lst[i * 2]    # 첫 번째 학생 번호
        snd = lst[i * 2 + 1]  # 두 번째 학생 번호
        union(fst, snd)    # 두 학생이 같은 조에 속하도록 합침

    # 각 학생의 대표를 찾고 집합의 수를 세기 위한 준비
    result = [find(i) for i in range(1, N + 1)]

    # 대표자 집합의 수를 계산하여 출력
    print(f'#{tc} {len(set(result))}')