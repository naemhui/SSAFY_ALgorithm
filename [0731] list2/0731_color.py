def coloring(r1, c1, r2, c2, color):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if arr[i][j] == 0 or arr[i][j] == color:
                arr[i][j] = color
            else:
                arr[i][j] = 3  # 보라색을 3으로 표시

T = int(input())

for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        coloring(r1, c1, r2, c2, color)
    
    # 보라색(3) 카운트
    purple_count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                purple_count += 1
    
    print(f'#{tc} {purple_count}')


# def coloring(list1, list2):
#     arr = [list([0]*10) for _ in range(10)]
#     count = 0

#     # list1: 빨강
#     n1, m1 = list1[0], list1[1]  # 시작 위치
#     n2, m2 = list1[2], list1[3]  # 끝 위치

#     for i in range(n1, m1+1):
#         for j in range(n2, m2+1):
#             arr[i][j] += 1
    
#     # list2: 파랑
#     n1, m1 = list2[0], list2[1]  # 시작 위치
#     n2, m2 = list2[2], list2[3]  # 끝 위치

#     for i in range(n1, m1+1):
#         for j in range(n2, m2+1):
#             arr[i][j] += 1

#     # arr을 돌아다니며 보라색 찾기
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j] == 2:
#                 count += 1

#     return count

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     for i in range(N):
#         list1 = list(map(int, input().split()))
#         list2 = list(map(int, input().split()))

#     result = coloring(list1, list2)    
#     print(f'#{tc} {result}')