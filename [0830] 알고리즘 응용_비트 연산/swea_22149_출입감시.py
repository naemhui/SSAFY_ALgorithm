# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())  # 저장된 id 개수
#     id_lst = list(map(int, input().split()))
#
#     arr = [0]*max(id_lst)
#
#     for i in id_lst:
#         arr[i-1] += 1
#     # print(arr)
#
#     for i in range(len(arr)):
#         cnt = arr[i]
#         if cnt%2 != 0:
#             print(f'#{tc} {i+1}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 저장된 id 개수
    id_lst = list(map(int, input().split()))

    zero = 0
    for i in id_lst:
        zero = zero ^ i
    print(f'#{tc} {zero}')

# i = 3 zero 3
# i = 2 zero 3 2