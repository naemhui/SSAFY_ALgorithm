# def BubbleSort(lst, n):
#     for i in range(n-1, 0, -1):
#         for j in range(0, i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
#
#
# T = int(input())
#
# for tc in range(T):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))
#
#
#     BubbleSort(lst, N)
#
#     max_v = sum(lst[(-1)*M:])
#     min_v = sum(lst[:M])
#     result = max_v - min_v
#     print(f'#{tc+1} {result}')


def differ(lst, M):
    min_v = lst[:M]
    max_v = lst[-M:]
    for i in range(len(lst)-M):
        if min_v >= sum(lst[i:M]):
            min_v = sum(lst[i:M])
        if max_v <= sum(lst)



DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5

N = len(DATA)  # DATA의 크기
TEMP = [0] * N  # 정렬 결과 저장

# 1단계: DATA 원소 별 개수 세기
# DATA의 원소 x룰 가져와서 COUNTS[x]의 개수 기록
for x in DATA:
    COUNTS[x] += 1
