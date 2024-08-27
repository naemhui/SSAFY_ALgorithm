'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def pre_order(T):
    if T:
        print(T, end = ' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input())        # 1번부터 N번까지인 정점
E = N-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1)       #
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
# for i in range(0,E*2, 2):
#         p, c = arr[i], arr[i + 1]
    if left[p]==0:          # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)



# N = int(input())
# arr = list(map(int, input().split()))

# # 인덱스가 부모 노드의 번호인 배열 두 개 준비
# cleft = [0]*(N+1)  # cleft[1] => 1번노드의 왼쪽 자식 노드 번호
# cright = [0]*(N+1)  # cright[1] => 1번 노드의 오른쪽 자식 노드 번호
# parent = [0]*(N+1)


# for i in range(N-1):
#     parent = arr[i*2]
#     child = arr[i*2+1]

#     # parent 노드의 왼쪽이 비었으면 왼쪽부터
#     if cleft[parent]:
#         cleft[parent] = child
#     # 왼쪽에 누가 있으면 오른쪽으로
#     else:
#         cright[parent] = child


# # 1. 전위순회 preorder V-L-R
# def preorder(t):
#     # 현재 노드 번호가 t일 때
#     # t번 노드가 존재하는가?
#     if t:
#         # t번 노드 방문처리
#         print(t, end=" ")
#         ##########
#         # 왼쪽
#         preorder(cleft[t])
#         # 오른쪽
#         preorder(cright[t])
# preorder(1)
# print()

# # 2. 중위순회
# def inorder(t):
#     # 현재 노드 번호가 t일 때
#     # t번 노드가 존재하는가?
#     if t:
#         # t번 노드 방문처리
#         print(t, end=" ")
#         ##########
#         # 왼쪽
#         inorder(cleft[t])
#         # 오른쪽
#         inorder(cright[t])
# inorder(1)
# print()

# def postorder(t):
#     # 현재 노드 번호가 t일 때
#     # t번 노드가 존재하는가?
#     if t:
#         # t번 노드 방문처리
#         print(t, end=" ")
#         ##########
#         # 왼쪽
#         postorder(cleft[t])
#         # 오른쪽
#         postorder(cright[t])
# postorder(1)
# print()







