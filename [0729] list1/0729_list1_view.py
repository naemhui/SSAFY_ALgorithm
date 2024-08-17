## 처음으로 출력값 제대로 나온 코드: 근데 런타임 오류 뜸
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     length = list(map(int, input().split()))
#     lst = []

#     for i in range(0, n - 2):

#         if (length[i + 2] > length[i + 1]) and (length[i + 2] > length[i]):
#             if (length[i + 2] > length[i + 3]) and (length[i + 2] > length[i + 4]):
#                 max_lenth = max([length[i], length[i + 1], length[i + 3], length[i + 4]])
#                 lst.append(length[i + 2] - max_lenth)
#     result = sum(lst)
#     print(f'#{_+1} {result}')



## 함수로 만들면 런타임 오류 안 뜸
def count_view(length):
    lst = []

    for i in range(0, n - 2):

        if (length[i + 2] > length[i + 1]) and (length[i + 2] > length[i]):
            if (length[i + 2] > length[i + 3]) and (length[i + 2] > length[i + 4]):
                max_lenth = max([length[i], length[i + 1], length[i + 3], length[i + 4]])
                lst.append(length[i + 2] - max_lenth)
    result = sum(lst)
    return result


# 테스트 케이스 처리
t = 10

for i in range(t):
    n = int(input())
    length = list(map(int, input().split()))
    
    count = count_view(length)
    print(f"#{i+1} {count}")



# # 테스트 케이스 처리
# t = 10
# results = []

# for i in range(t):
#     n = int(input())
#     length = list(map(int, input().split()))
    
#     count = count_view(length)
#     results.append(f"#{i+1} {count}")

# # 결과 출력
# for result in results:
#     print(result)


# import sys
# sys.stdin = open('sample_input (1).txt', 'r')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
###########################################
# for 건물 in 강물:
#     for 층 in 건물:
#         if 층이 조망권:
#             개수 + 1



# def count_view_apartments(buildings):
#     count = 0
#     for i in range(2, len(buildings) - 2):
#         left_max = max(buildings[i-2], buildings[i-1])
#         right_max = max(buildings[i+1], buildings[i+2])
#         surrounding_max = max(left_max, right_max)
        
#         if buildings[i] > surrounding_max:
#             count += buildings[i] - surrounding_max
    
#     return count




#### clude
# def count_view_apartments(buildings):
#     count = 0
#     for i in range(2, len(buildings) - 2):
#         left_max = max(buildings[i-2], buildings[i-1])
#         right_max = max(buildings[i+1], buildings[i+2])
#         surrounding_max = max(left_max, right_max)
        
#         if buildings[i] > surrounding_max:
#             count += buildings[i] - surrounding_max
    
#     return count

# # 테스트 케이스 처리
# test_cases = 10
# results = []

# for case in range(1, test_cases + 1):
#     width = int(input())
#     buildings = list(map(int, input().split()))
    
#     view_count = count_view_apartments(buildings)
#     results.append(f"#{case} {view_count}")

# # 결과 출력
# for result in results:
#     print(result)


