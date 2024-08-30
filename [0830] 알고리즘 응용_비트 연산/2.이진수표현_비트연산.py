# 두 개의 변수 M과 N을 가정하고, M의 하위 N 비트가 모두 1인지 확인
def solution():
    # 하위 N비트가 모두 1로 설정된 mask 생성
    mask = (1 << N) - 1
    # M의 하위 N비트가 모두 1인지 확인: M의 하위 N비트가 모두 1이어야만 True 반환
    return (M & mask) == mask


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solution()
    if result:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')