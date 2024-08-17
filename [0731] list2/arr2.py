# arr1 = [0] * 3
# # 0으로 채워진 일차원 배열을 반복해서 2*3 2차원 배열 만들기
# arr2 = [[0]*3 for _ in range(2)]
# print(arr1)
# print(*arr1)  # 언팩

## 밑에 코드처럼 만들면 2차원 배열이 아님!!!!!!##
# arr = [[0]*3]*2
# print(arr)
# arr[0][0] = 1
# print(arr)

###############################
# # 2차원은
# for i in range(2):
#     # print(arr2[i])  # 1행 전체를 의미
#     print(*arr2[i])
#
# for i in range(2):
#     for j in range(3):
#         print(arr2[i][j], end = ' ')
#     print()


# arr = [[1, 2, 3], [4, 5, 6]]
# print(len(arr))  # 행 개수
# print(len(arr[0]))  # 열 개수
#
# # s = 0
# # for i in range(n):
# #     for j in range(m):
# #         s += arr[i][j]
#
# # 행의 합 or ~~ 합
#
# # 여기에서 sum 초기화 하면 전체 합?
# for j in range(m):
#     # 여기에서 sum 초기화 하면 행의 합
#     for i in range(n):
#         f(array[i][j])  # 필요한 연산 수행
#
# for i in range(n):
#     for j in range(m):
#         f(array[i][j + (m-1-2*j)*(i%2)])
#
#
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(3):
#     for j in range(3):
#         if i < j:  # 중복 방지 !
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# # 당분간은 zip 사용 금지


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for i in range(N):
    total = 0
    for j in range(N):  # NxN 배열의 모든 원소에 대해
        s = 0  # 문제에서 원소와 인접원소의 차의 ... 합
        # i, j 원소의 네 방향(여기서는 상하좌우) 원소에 대해!
        for k in range(4):
            ni = i+di[k]  #
            nj = j+dj[k]
            if 0<= ni< N and 0<=nj< N:  # 이 코드에서 오류 많이 냄
                s += abs(arr[i][j] - arr[ni][nj])  # 실존하는 인접 원소 ni, nj가 구해진 것
        total += s
# print(arr)

# 유한 개의