'''
식재료를 N/2씩 나누어 요리
두 맛의 차이가 최소가 되도록 해야 함
'''

import sys
sys.stdin = open('sample_input (3).txt', 'r')


# 식재료 시너지 계산
def food_synergy(ingred):
    synergy = 0
    for i in range(len(ingred)):
        for j in range(i + 1, len(ingred)):
            synergy += arr[ingred[i]][ingred[j]] + arr[ingred[j]][ingred[i]]
    # print('synergy:', arr[ingred[i]][ingred[j]], arr[ingred[j]][ingred[i]], synergy)
    return synergy


# lev가 N // 2에 도달하면
# 각 식재료를 두 음식으로 배분하여 만듦
def making_food(lev, start):
    global min_diff
    if lev == N // 2:
        food_A = food
        food_B = [i for i in range(N) if i not in food_A]
        # print('food_a', food_A, 'food_b', food_B)

        A_synergy = food_synergy(food_A)
        B_synergy = food_synergy(food_B)

        diff = abs(A_synergy-B_synergy)
        min_diff = min(min_diff, diff)
        # print(food_A, food_B, min_diff)
        return

    for i in range(start, N):
        food.append(i)
        making_food(lev + 1, i + 1)
        food.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')  # 시너지 최솟값 초기 설정
    food = []
    making_food(0, 0)
    print(f'#{tc} {min_diff}')