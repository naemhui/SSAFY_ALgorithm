def max_diag(arr):
    sum_lst = []

    # 각 행의 합
    for i in range(100):
        sum_lst.append(sum(arr[i]))  # 각 행의 합 -> sum_lst

    # 각 열의 합
    for j in range(100):
        col_lst = []
        for i in range(100):
            col_lst.append(arr[i][j])
        sum_lst.append(sum(col_lst))

    # 대각선의 합
    dia1_sum = 0
    for i in range(100):  
        for j in range(100):
            if i == j:
                dia1_sum += arr[i][j]
    sum_lst.append(dia1_sum)
        
    dia2_sum = 0    
    for i in range(100):  
        for j in range(100):  
            if i + j == 99:
                dia2_sum += arr[i][j]
    sum_lst.append(dia2_sum)

    return max(sum_lst)

                
               

import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    result = max_diag(arr)

    print(f'#{tc} {result}')
