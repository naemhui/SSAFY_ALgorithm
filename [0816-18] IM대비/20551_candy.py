'''
A개 B개 C개

'''

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    # 이미 조건 만족
    if A < B and B < C:
        print(f'#{tc}', 0)

    # 절대 조건 만족 X
    elif B == 1 or C == 1 or C == 2:
        print(f'#{tc}',-1)

    # 나머지 상황 테스트
    else:
        if B == C:
            if A < B:
                B -= 1
                if A == B:
                    A -= 1
                    print(f'#{tc}',2)
                elif A < B:
                    print(f'#{tc}',1)

            elif A == B:
                # B -= 1
                # A -= 2
                print(f'#{tc}',3)

            elif A > B:
                B -= 1
                cnt = 1 + A - B + 1
                print(f'#{tc}',cnt)

        elif B < C:
            if A > B:
                # A -= A - B + 1
                print(f'#{tc}',A - B + 1)
            elif A == B:
                A -= 1
                print(f'#{tc}',1)

        elif B > C:
            if A == B:
                cnt = B - C + 1
                B -= B - C + 1
                cnt += A - B + 1
                A -= A - B + 1
                print(f'#{tc}', cnt)
            elif A < B:
                cnt = B - C + 1
                B -= B - C + 1
                if A == B:
                    cnt += 1
                    print(f'#{tc}', cnt)
                elif A > B:
                    cnt += A - B + 1
                    A -= A - B + 1
                    print(f'#{tc}', cnt)
                elif A < B:
                    print(f'#{tc}', cnt)