import sys
sys.stdin = open("in.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    dia_sum = 0  # 대각선 
    for i in range(N):
        for j in range(N):
            if i == j:
                dia_sum += arr[i][j]
            elif i + j == N-1:
                dia_sum += arr[i][j]
    print(dia_sum)