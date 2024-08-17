# def f(i, N):  # i 현재 인덱스, N크기
#     if i == N:  # 배열을 벗어난 경우
#         return
#
#     else:  # 구분을 해주기 위해 if else 구조 쓴 거고 안 써도 됨
#         print(arr[i])
#         f(i+1, N)
#         return

# 위와 같은 구조임!!! 응용버전
def f(i, N):
    if i == N:
        return

    print(arr[i])
    f(i+1, N)

arr = [1, 2, 3]  # 배열은 global 안 써도 잘 접근 됨
N = 3
f(0, N)