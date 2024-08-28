N = int(input())
tree = [0]*(N+1)
left = [0] * (N + 1)
right = [0] * (N + 1)

result = 0

for tc in range(1, N+1):
    # 정점 번호, 양의 정수
    lst = list(input().split())
    tree[int(lst[0])] = lst[1]

    if len(lst) != 2:
        # lst[0], lst[2], lst[3] = int(lst[0]), int(lst[2]), int(lst[3])

        left[int(lst[0])] = lst[2]
        right[int(lst[0])] = lst[3]
        # left[lst[0]] = lst[2]
        # right[lst[0]] = lst[3]
    # else:
        # lst[0], lst[1] = int(lst[0]), int(lst[1])

    for i in range(N, 1, -1):
        calcul = tree[i//2] + tree[i]
        result += calcul
    print(tree)
    print(left)
    print(right)