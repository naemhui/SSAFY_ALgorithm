# T = int(input())
# for tc in range(1, T=1):
#     E, N = map(int, input().split())
#     arr = list(map(int, input().split()))

#     cleft = [0]*(E+2)
#     cright = [0]*(E+2)

#     for i in range(E):
#         parent = arr[i*2]
#         child = arr[i*2+1]

#         if cleft[parent] == 0:
#             cleft[parent] = child

#         else:
#             cright[parent] = child

#####
# 16692
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0]*(N+1)
    cleft = [0]*(N+1)
    cright = [0]*(N+1)

    for i in range(2, N+1):
        