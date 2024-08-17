# for _ in range(3):
# print(data)

# n, m = map(int, input().split())
# data = []
# for _ in range(n):
#     string = input()
#     data.append(string)
# # print(data)

# i = 0
# j = 1
# M = 2
# text = [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3']]
# result1 = "".join(list(zip(*text))[i][j:j+M])
# print(result1)
#
# result2 = ""
# for l in range(M):
#     result2 += text[j+l][i]
# print(result2)

# i = 0
# j = 1
# M = 2

# text = [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3']]

# # result1 = "".join(list(zip(*text))[i][j:j+M])
# result1 = "".join(list(zip(*text))[0][1:3])
# print(zip(*text))
# print(list(zip(*text)))
# print(list(zip(*text))[0])
# print(list(zip(*text))[0][1:3])
# print(result1)

# dict = {}
# str1 = 'ABCA'
# str2 = 'ABABCA'

# for i in range(len(str1)):
#     dict[str1[i]] = 0
# print(dict)
# print(dict.keys())
# for _ in dict.keys():
#     print(_)

# def max_count(str1, str2):
#     dict = {}
#     for alphabet in str1:
#         dict[alphabet] = 0
#     # 여기까지 하면 {'A':0, 'B':0, ...} 이런 식으로 만들어짐
    
#     for alphabet in str2:
#         for _ in dict.keys():
#             if alphabet == _:
#                 dict[_] += 1
#     # 이제 {알파벳: count} dict 만들어짐

#     max_count = 0
#     for count in dict.values():
#         if count > max_count:
#             max_count = count
#     return max_count

# print(max_count(str1, str2))
dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

T = int(input())
for tc in range(1, T):
    input_num = input()
    data = list(map(str, input().split()))

    lst = []
    for num in data:
        lst.append(dict[num])
    print(lst)