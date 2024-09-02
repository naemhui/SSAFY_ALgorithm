path = []

# cnt 는 하지 않을게요. 경로를 출력하는 걸로 코드 짜볼게요.

# 주사의 몇 개 던졌는지. 주사위 합이 몇인지
def kfc(level, total):
    if total > 10:
        return

    # 기저조건: 3개를 던졌을 때 종료
    if level == 3:
        # 10 이하인가?
        if total <= 10:
            print(f'{path} = {total}')

        return

    # 후보군 탐색
    for i in range(1, 7):
        # i는 주사위 숫자
        path.append(i)
        kfc(level + 1, total + i)  # total은 0인 상태로부터 주사위 결과를 더하여 전달
        path.pop()

kfc(0, 0)
