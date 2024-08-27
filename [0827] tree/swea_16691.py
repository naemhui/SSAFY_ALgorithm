cnt = 0
# 1. 전위순회 preorder V - L - R
def preorder(t):
    global cnt
    # 현재 노드 번호가 t 일때
    # t번 노드가 존재 하는가?
    if t:
        # t번 노드 방문 처리
        # print(t, end=" ")
        cnt += 1
        ####################
        # 왼쪽
        preorder(cleft[t])
        # 오른쪽
        preorder(cright[t])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 인덱스가 부모 노드의 번호인 배열 두개 준비
    cleft = [0] * (E+1 + 1)  # cleft[1] ==> 1번노드의 왼쪽 자식 노드 번호
    cright = [0] * (E+1 + 1)  # cright[1] ==> 1번노드의 오른쪽 자식 노드 번호

    for i in range(E+1 - 1):
        parent = arr[i * 2]
        child = arr[i * 2 + 1]

        # parent 노드의 왼쪽이 비었으면 왼쪽부터
        if cleft[parent] == 0:
            cleft[parent] = child

        # 왼쪽에 누가 있으면 오른쪽으로
        else:
            cright[parent] = child

    preorder(N)
    print(f'#{tc} {cnt}')
    cnt = 0