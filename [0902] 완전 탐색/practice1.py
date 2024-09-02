# 1.
for i in range(1, 4):
    for j in range(1, 4):
        print(int(str(i)+str(j)))

# 2.
# def KFC(n):
#     # print(n)
#     KFC(n+1)
#
# KFC(0)
# print('끝')

# 3.
def func(x):
    # 1. 기저조건(종료조건)
    if x == 6:
        return

    ## 다음의 3가지가 필요함!
    # 2. 다음 재귀호출 전
    print(x, end=' ')
    # 3. 재귀호출 (현재 값에 무슨 수식을 적용해서 넘겨줄까?)를 고려하여 다음 줄 작성
    func(x+1)  # 다음 재귀 호출에서는 현재보다 x값이 1 커야 한다.
    # 4. 호출하고 돌아왔을 때
    # 이 시점에서 x는 5이기 때문에 그대로 출력하면 됨
    print(x, end=' ')
start = 0
func(start)