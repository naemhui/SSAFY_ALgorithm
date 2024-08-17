
# i~j번까지 사람들 중 승자를 정하고 게임결과 정하기
def tournament(i, j):
    # 분할: 문제를 쪼갤 수 있을 때까지 계쏙 쪼갬
    # 쪼갤 수 엇ㅂ으면 돌아가
    if i==j:
        # 시작과 끝이 같으면 쪼개기 불가
        return i
    else:
        # 문제를 왼쪽 부분과 오른쪽 부분으로 쪼갠다
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2+1, j)
        # 각각 쪼갤 수 있을 때까지 계----속 쪼개\
        return 왼오 승자