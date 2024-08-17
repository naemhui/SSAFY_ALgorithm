# 재귀합수 통해 2차원 배열 행 우선 순회해보기
#
# N = 5
# arr = [[N*j + i for i in range(1, N+1)] for j in range(N)]  # 1~25
# print(arr)
# # 12345
# # 678910


# 강사님's 재귀함수
# 시작: 0,0 -> 0,1 -> 0,2
# 1,0 => 1,1 ..
# 재귀호출이 진행될 때마다 바뀌는 변수(어떤 값) ??
# 종료 4,4
N = 5
arr = [[N*j + i for i in range(1, N+1)] for j in range(N)]

def myprint(r, c, N):

    # 종료 조건
    if r == N:
        return

    print(arr[r][c], end=" ")

    # 재귀 호출(인자를 변경시켜 종료 조건을 향해서 가도록)
    nr, nc = r, c
    if c + 1 < N:
        nc = c + 1
    else:
        # 다음 줄로 가렴
        print()
        nc = 0
        nr = r + 1

    myprint(nr, nc, N)

myprint(0, 0, 5)

# 나의 잘못된 재귀함수
# def my_print(N, i):
#     if i == N:
#         return
#
#     answer = [N*i+j for j in range(1, N+1)]
#     print(answer, end = ' ')
#     return my_print(N, i+1)
#
#
# N = 5
# arr = my_print(N, 0)

# print(arr)



## 학선's 재귀함수
# N = 5
# arr = [[N*j + i for i in range(1, N+1)] for j in range(N)]
#
# def recul(i, j, N):
#     if i > N-1:
#         return
#     elif j > N-1:
#         print()
#         return recul(i+1, 0, N)
#     else:
#         print(arr[i][j], end=" ")
#
#     recul(i, j+1, N)  # 안 벗어나면 열 번호만 +1
# recul(0, 0, N)