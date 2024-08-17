s = 'abcdef'
# a+b+c+d+e+f
# 뒤집으려면
# f+e+d+c+b+a  -> 즉, 반복문을 뒤에서부터 돌기만 하면 됨

# s를 뒤집기(반복문 사용)
s_reverse = ''
for i in range(len(s)):
    s_reverse += s[len(s)-1-i]  # -1이라는 인덱스는 알고리즘 풀 때 쓰지마
    # 알고리즘을 푸는 도구로써 파이썬 이용하는 것일 뿐임
print(s_reverse)
print(s[::-1])

# ord
s1 = 'abb'
s2 = 'abc'
print(ord('b'))
print(ord('c'))
print(s1>s2)  # 사전순. abb가 앞, abc가 뒤
# 파이썬에서 비교할 때 크기를 비교하는 것. 문자열도 내부적으로는 숫자로 바꾸어서 비교

