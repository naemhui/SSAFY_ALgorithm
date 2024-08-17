# n = int(input())
# data = list(map(int, input().split()))

# # max_v = data[0]
# # min_v = data[0]

# lst = []

# for _ in range(10):
#     lst.append(data.remove(max(data)))
#     lst.append(data.remove(min(data)))
# print(lst)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = int(input())
# data = list(map(int, input().split()))

# max_v = data[0]
# min_v = data[0]

lst = []

while len(lst) < 11:
    lst.append(max(data))
    data.remove(max(data))
    if len(lst) == 10:
        break
    lst.append(min(data))
    data.remove(min(data))
print(lst)