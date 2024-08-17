# import sys
# a = ''  # 49: 내용이 없더라도 스트링이니까 49바이트를 기본으로 사용
# b = 'a'  # 50
# c = 'ab'  # 51
# d = 'abc'  # 52
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))
#
# s1 = list(input())
# s2 = input()
# print(s1)
# print(s2)
# print(s1[0])
# print(s2[0])
#
# s = input()  # iterable
# print(s[0])
# print(s[1])
#
# s1 = 'abc'
# s1[0] = 'A'
# print(s1[0])
# s2 = 'Abc'
# print(s2)
#
# s1 = list(input())
# s2 = input()
# s1[0] = 'A'
# print(s1[0])
# s2[0] = 'A'
# print(s2[0])  # error
#
# s1 = 'abc'
# s2 = 'abc'
# print(s1 == s2)  # 내용 비교
#
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# print(l1 == l2)
#
# s3 = s1[:2] + 'c'
# print(s3)
# print(s2 == s3)  # True
# print(s2 is s3)  # False
# print(s1 is s2)  # True
#
#
# s1 = 'A'
# print(ord('A'))  # 65
# print(ord(s1))
# print(chr(65))  # A
#
# ## 연습문제2
# a = 123
# str(b, a)
# print(b) # '123'
#
# '==' 자바랑 파이썬에서 다른 역할!!!
# 인코딩이 뭔지!!