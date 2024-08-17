# 파이썬에서 리스트 메서드 이용해서 스택 만들기

# 1. 스택 초기화(선언)
# 내가 이 빈 리스트를 스택으로 사용하겠다.
s = []

# 스택에 원소 삽입하기
for i in range(10):
    s.append(i)  # append가 stack push랑 똑같음

print(s)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 스택에 원소 삭제하기 : pop
for i in range(10):
    print(s.pop(), end = ",")  # 9,8,7,6,5,4,3,2,1,0,
print()

print(s)  # []

# 스택에서 원소를 모두 꺼내고 싶은데 몇 개 있는지 몰라
# for i in range(len(s))  # 이렇게 하면 되긴 하겠지만 len 안 쓰고 어떻게 하냐면!!!!
# [] 빈 리스트는 False로 취급됨
while s:
    # s 안에 뭔가가 남아있다면 아래 문장 실행
    print(s.pop(), end = " ")
print()
print(s)