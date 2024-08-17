# 끝 지점부터 반대로 올라가서 답을 찾아보자.
# import sys
# sys.stdin = open('input_data/ladder1.txt', 'r')
for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            x = i
            break
    # 현재 열 위치는 x

    # 아래에서부터 1을 찾아 올라감
    for y in range(99, 0, -1):
        # 왼쪽에 1이 있을 때
        if x - 1 >= 0 and arr[y][x - 1] == 1:  # 범위 필요 (x가 0인 경우 오류)
            # 왼쪽 값이 1인 동안 x -= 1
            while x - 1 >= 0 and arr[y][x - 1] == 1:
                x -= 1

        # 오른쪽에 1이 있을 때
        elif x + 1 <= 99 and arr[y][x + 1] == 1:
            while x + 1 <= 99 and arr[y][x + 1] == 1:
                x += 1

    print(f'#{tc} {x}')