'''
완전탐색 하면 된다
말 그대로 순열로 푸는 문제
대신 + - * /밖에 없기 때문에 중복해서 선택할 수 있도록 만들어야 함

완전탐색부터 고려를 할 것 DFS BFS brute force 하지만 시간 메모리 초과 조심
효율적인 자료구조는 없는가 stack queue heap 안되면
백트래킹 .. 시간을 줄이는 방법 떠올리기 (조건문) 아니면
그리디 DP 규칙이나 재사용되는 요소들. 재계산 줄이는 법
추가적인 알고리즘
'''

import sys
sys.stdin = open('input.txt', 'r')

'''
마이너스 반례
1
3
0 1 0 1
3 5 3
'''


def cal(num1, num2, oper_idx):
    if oper_idx == 0:
        return num1 + num2

    if oper_idx == 1:
        return num1 - num2

    if oper_idx == 2:
        return num1 * num2

    if oper_idx == 3:
        if num1 < 0:  # 음수처리
            return -(abs(num1) // num2)
        return num1 // num2


# 재귀 설계
# 시작점: 첫 번째 숫자
# 끝점: 모든 수(연산자)를 사용할 때 까지
# 파라미터: 특정 시점에서 계산된 결과값
def dfs(level, total):
    global min_result, max_result

    if level == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 4개의 연산자를 확인
    for i in range(4):
        if opers[i] == 0:  # 남은 연산자가 없으면 통과
            continue

        opers[i] -= 1
        dfs(level + 1, cal(total, numbers[level], i))
        opers[i] += 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_result = 1e9
    max_result = -1e9

    dfs(1, numbers[0])
    print(f'#{tc} {max_result - min_result}')

