def evaluate_tree(tree, left, right, node):
    # 만약 현재 노드가 연산자라면
    if tree[node] in '+-*/':
        left_value = evaluate_tree(tree, left, right, left[node])
        right_value = evaluate_tree(tree, left, right, right[node])
        # 연산자에 따라 결과를 계산합니다
        if tree[node] == '+':
            return left_value + right_value
        elif tree[node] == '-':
            return left_value - right_value
        elif tree[node] == '*':
            return left_value * right_value
        elif tree[node] == '/':
            return left_value / right_value
    else:
        # 현재 노드가 숫자라면
        return float(tree[node])

for tc in range(1, 11):
    N = int(input())  # 노드의 개수
    tree = [None] * (N + 1)  # 노드 값 저장
    left = [0] * (N + 1)  # 왼쪽 자식 저장
    right = [0] * (N + 1)  # 오른쪽 자식 저장

    for _ in range(1, N+1):
        lst = input().split()
        node = int(lst[0])  # 노드 번호

        if len(lst) == 2:
            # 숫자 노드의 경우
            tree[node] = lst[1]
        elif len(lst) == 4:
            # 연산자 노드의 경우
            tree[node] = lst[1]
            left[node] = int(lst[2])
            right[node] = int(lst[3])

    result = evaluate_tree(tree, left, right, 1)
    print(f'#{tc} {int(result)}')
