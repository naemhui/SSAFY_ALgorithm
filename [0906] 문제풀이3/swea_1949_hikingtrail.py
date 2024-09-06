'''
부지는 N*N
1. 가장 높은 봉우리에서 시작
2. 높은 지형 -> 낮은 지형 : 가로 또는 세로로 연결
3. 딱 한 곳만 정해서 최대 K만큼 지형 깎을 수 있음
'''
# import sys
# sys.stdin = open('sample_input (3).txt', 'r')


# 델타 탐색: 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(i,j,N):
    return 0<=i<N and 0<=j<N

# 이전 칸과 비교하여 다음 칸이 몇 칸 낮은지 확인 (4->3이라면 1 return)
def differ(r,c, nr,nc):
    return arr[r][c] - arr[nr][nc]


check = True
def making_trail(r,c):
    global cnt
    global max_cnt
    global check

    # 1. 다음 칸으로 갈 수 있을 때
    if differ(r,c,nr,nc) == 1:
        cnt += 1
        # print(cnt)
        print(f'#1번 {nr} {nc} {cnt}')
        making_trail(nr,nc)
        max_cnt = max(max_cnt, cnt)

    # 2. 깎으면 다음 칸으로 갈 수 있을 때
    elif 1 < differ(r,c,nr,nc) <= K and check:
        check = False
        arr[nr][nc] = arr[r][c] -1
        cnt += 1
        print(f'#2번 {cnt}')
        making_trail(nr,nc)
        max_cnt = max(max_cnt, cnt)

    # 다음 칸으로 절대 못 갈 때
    else:
        cnt = 1
        print(f'#3번 {cnt}')
        making_trail(nr,nc)
        # continue
    #     cnt = 0
    #     making_trail(nr,nc)


    return max_cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for r in range(N):
        for c in range(N):
            cnt = 1
            max_cnt = 1
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr, nc, N):
                    cnt = making_trail(r,c)
            answer = max(answer, cnt)

    print(f'#{tc} {answer}')