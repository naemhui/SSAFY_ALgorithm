T = int(input())

for tc in range(1, T+1):
    P = input()
    T = input()

    result = 0

    pl = len(P)
    tl = len(T)

    pi = 0
    ti = 0

    while pi < pl and ti < tl:
        if T[ti] != P[pi]:
            ti = ti - pi  # 텍스트 비교 시작 위치
            pi = -1

        ti += 1
        pi += 1

        if pi == pl: # 패턴을 발견했다!            
            result = 1

    print(f'#{tc} {result}')