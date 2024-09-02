'''
최대로 고려해야 하는 경우의 수:
2개 선택해서 위치 교환 가능
교환 중복 가능

최대 6자리, 최대 교환 횟수는 10
경우의 수 줄이는 방법:

종료 조건, 호출 전, 재귀호출, 돌아왔을 때,
'''
cnt = 0
def func(card, i, opp):
    n_card = card[:len(card)-i]
    global cnt
    if cnt == opp:
        # print(card)
        return card

    min_i = n_card.index(min(n_card))  # 가장 작은 숫자의 인덱스
    if min_i != len(card)-1:  # 가장 작은 숫자의 인덱스가 맨 뒤가 아니라면
        # card[-1], card[min_i] = card[min_i], card[-1]
        card[-1-i], card[min_i] = card[min_i], card[-1-i]
        cnt += 1
        func(card, i+1, opp)
    else:
        card[min_i], card[min_i-1] = card[min_i-1], card[min_i]
        cnt += 1
        func(card, i+1, opp)

cnt = 0
T = int(input())
for tc in range(1, T + 1):
    card_str, opp = input().split()
    card = [int(char) for char in card_str]
    opp = int(opp)
    result = func(card, 0, opp)
    print(f'#{tc} {result}')
    
# cnt = 0
# def func(card, i, opp):
#     global cnt

#     # 종료 조건
#     if cnt == opp:
#         return int(''.join(map(str, card)))

#     length = len(card)
#     max_value = int(''.join(map(str, card)))

#     for x in range(length):
#         for y in range(x + 1, length):
#             # 위치 x와 y의 카드를 교환합니다.
#             card[x], card[y] = card[y], card[x]

#             # 교환 횟수를 증가시키고 재귀 호출
#             cnt += 1
#             max_value = max(max_value, func(card, i + 1, opp))
#             cnt -= 1

#             # 원상 복구
#             card[x], card[y] = card[y], card[x]

#     return max_value

# result = func([2, 7, 3, 7], 0, 1)

# cnt = 0
# T = int(input())
# for tc in range(1, T + 1):
#     card_str, opp = input().split()
#     card = [int(char) for char in card_str]
#     opp = int(opp)
#     result = func(card, 0, opp)
#     print(f'#{tc} {result}')


# def dfs(depth):
#     global ans

#     if depth == M:
#         ans = max(ans, int(''.join(arr)))
#         return

#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             arr[i], arr[j] = arr[j], arr[i]

#             check = int(''.join(arr))
#             if (depth, check) not in visited:
#                 visited.append((depth, check))
#                 dfs(depth + 1)

#             arr[i], arr[j] = arr[j], arr[i]


# result = []
# T = int(input())
# for case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(str(N))
#     visited = []
#     ans = 0
#     dfs(0)

#     result.append(f"#{case} {ans}")
# for _ in result:
#     print(_)

def dfs(depth, i, j):
    global ans, cnt

    if depth == M:
        ans = max(ans, int(''.join(arr)))
        return

    if i >= len(arr) - 1:
        return

    if j >= len(arr):
        dfs(depth, i + 1, i + 2)
        return

    # 두 자리를 교환
    arr[i], arr[j] = arr[j], arr[i]

    check = int(''.join(arr))
    if (depth, check) not in visited:
        visited.append((depth, check))
        dfs(depth + 1, 0, 1)

    # 원래대로 복구
    arr[i], arr[j] = arr[j], arr[i]

    # 다음 자리로 이동
    dfs(depth, i, j + 1)


result = []
T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(str(N))
    visited = []
    ans = 0
    dfs(0, 0, 1)

    result.append(f"#{case} {ans}")
for _ in result:
    print(_)
