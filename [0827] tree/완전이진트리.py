'''
6
ABCDEF
'''
# 완전 이진 트리에 완전 유용한 방법
def preorder(root_idx):
    if root_idx <= N:
    # if tree[root_idx]:
        print(tree[root_idx])
        preorder(2*root_idx)
        preorder(2*root_idx+1)

def inorder(root_idx):
    if root_idx <= N:
        inorder(2*root_idx)
        print(tree[root_idx])
        inorder(2*root_idx+1)

def postorder(root_idx):
    if root_idx <= N:
        postorder(2*root_idx)
        postorder(2*root_idx+1)
        print(tree[root_idx])

N = int(input())
arr = input()

tree = [0] * (N+1)
for i in range(len(arr)):
    tree[i+1] = arr[i]

print(tree)
postorder(1)