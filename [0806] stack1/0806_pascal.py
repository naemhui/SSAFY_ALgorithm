# def pascal(N):
#     if N == 1:
#         return [1]
#     # arr = [[1] * (i + 1) for i in range(N)]
#     arr = [1] * N
#     print(arr)
#     return pascal(N-1)
#
# print(pascal(5))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * (i + 1) for i in range(N)]


    for i in range(N):
        for j in range(0, i+1):
            if j == 0 or j == i:
                arr[i][j] += 1

    for i in range(2, N):
        for j in range(1, i):  # 0부터 i-1까지

            for k in range(j-1, j+1):
                arr[i][j] += arr[i-1][k]
    print(f'#{tc}')
    # print(arr)
    for i in range(N):
        print(*arr[i])
    # # for _ in arr:
    # #     print(' '.join(map(str, _)))



