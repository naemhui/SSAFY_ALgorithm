# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)

# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end = ",")
#     print()
# print()


# def subset(number_set):
#     n = len(number_set)
    
#     for i in range(0, 1<< n):  # 0부터 2^n-1까지 -> 0~7까지
#         subset = []

#         # 부분집합 만드는 중~
#         for j in range(n):
#             if i & (1<<j):
#                 subset.append(number_set[j])
#         print(subset, end = ",")

# subset([1, 2, 3])

# data = set(range(1, 13))
# print(data)
# arr = [list([0]*10) for _ in range(10)]
# arr[1][2] = 2
# # print(arr)

# arr1 = list([0]*5 for _ in range(5))
# arr1[1][2] = 2
# print(arr1)
# print(" ")
# arr2 = [list([0]*5) for _ in range(5)]
# arr2[1][2] = 2
# print(arr2)

print(list([0]*5))