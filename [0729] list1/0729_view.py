# 우리 강사님 풀이

T = 10

for tc in range(T):
    n = int(input())

buildings = list(map(int,input().split()))

count = 0

for i in range(2, n-2):
    height = buildings[i]  # i위치에 있는 건물의 높이
    for j in range(height, -1, -1):  # 위층부터 검사. 조망권 없는 위치 나오면 그 밑 볼 필요 없음
        if j > buildings[i-1] and j > buildings[i+1] and j > buildings[i+2]:
            count += 1
        else:
            # 만약 건물 하나라도 지금 층보다 높으면 검사 할 필요 없음
            break
    print(f'# {tc} {count}')