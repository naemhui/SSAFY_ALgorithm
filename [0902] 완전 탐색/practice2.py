'''
111
112
113
114
115
116
121
...
665
666
'''

################ my
path = []

def kfc(level):
    # 1.기저조건: 3개를 뽑은 경우 종료
    if level == 3:
        print(*path)
        return

    # 2. 1~6 후보군을 반복하며
    for i in range(1, 7):
        # 2.1 재귀 호출 전
        path.append(i)
        # 2.2 다음 재귀 호출 (파라미터 전달)
        kfc(level + 1)
        # 2.3 돌아왔을 때
        path.pop()

# 호출: 시작점을 같이 전달해주는 경우가 많다.
kfc(0)

################ pro
