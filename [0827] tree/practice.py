"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

9
1 2 1 3 2 4 2 5 3 6 3 7 5 8 5 9
"""

N = int(input())
arr = list(map(int, input().split()))
cleft = [0]*(N+1)
cright = [0]*(N+1)

for i in range(N-1):
    parent = arr[i*2]
    child = arr[i*2+1]

    if cleft[parent] == 0:
        cleft[parent] = child

    else:
        cright[parent] = child

def pre_order(t):
    if t:
        print(t, end=' ')
        pre_order(cleft[t])
        pre_order(cright[t])

pre_order(1)
print()


def in_order(t):
    if t:
        in_order(cleft[t])
        print(t, end=' ')
        in_order(cright[t])

in_order(1)
print()

def post_order(t):
    if t:
        post_order(cleft[t])
        post_order(cright[t])
        print(t, end=' ')
post_order(1)
print()