T = 10


# 후위 순회 진행
#  왼쪽 - 오른쪽 - 부모(자신)
def post_order(idx):
    # 해당 요소가 피연산자(숫자)이면 종료
    if str(tree[idx]) not in "+-/*":
        return tree[idx]

    a = post_order(left[idx])  # 왼쪽
    b = post_order(right[idx])  # 오른쪽
    # 부모(자기자신) 갱신
    if tree[idx] == "+":
        tree[idx] = a + b
    elif tree[idx] == "-":
        tree[idx] = a - b
    elif tree[idx] == "/":
        tree[idx] = a // b
    else:  # *
        tree[idx] = a * b

    return tree[idx]


for tc in range(1, T + 1):
    # 입력
    # 정점의 개수 N(1≤N≤1000)이 주어진다.
    N = int(input())

    # 트리를 표현할 수 있는 배열들 초기화 tree, left, right
    tree = [0] * (N + 1)  # 실질적인 노드 정보가 들어있는 배열
    left = [0] * (N + 1)  # 왼쪽 자식 노드 인덱스가 담겨있는 배열
    right = [0] * (N + 1)  # 오른쪽 자식 노드 인덱스가 담겨있는 배열
    # 그다음 N 줄에 걸쳐 각 정점의 정보가 주어진다.
    for _ in range(N):
        data = input().split()
        # 정점이 정수면 정점 번호와 양의 정수가 주어지고,
        if len(data) == 2:
            idx, val = map(int, data)
            tree[idx] = val
        # 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가 차례대로 주어진다.
        elif len(data) == 4:
            idx, oper, lchild, rchild = data
            idx, lchild, rchild = map(int, [idx, lchild, rchild])
            tree[idx] = oper
            left[idx] = lchild
            right[idx] = rchild

    # 정점 번호는 1부터 N까지의 정수로 구분되고
    # 루트 정점의 번호는 항상 1이다.
    # 로직 (후위 순회를 진행하며 노드 안에 값을 처리...)
    post_order(1)  # 루트 정점은 항상 1번부터(1번부터 순회)

    # 출력
    print(f"#{tc} {tree[1]}")