T = 10

for tc in range(1, T+1):
    input()

    P = input()  # 우리가 찾는 문자열
    T = input()  # 전체 텍스트

    count = 0

    pl = len(P)
    tl = len(T)

    pi = 0
    ti = 0

    while pi < pl and ti < tl:
        if T[ti] != P[pi]:
            ti = ti-pi  # 텍스트 비교 시작 위치
            pi = -1

        ti += 1
        pi += 1

        if pi == pl:
            count += 1

            ti = ti - pi + 1  # 다음 비교를 위해 시작 위치 + 1
            pi = 0

    print(f'#{tc} {count}')