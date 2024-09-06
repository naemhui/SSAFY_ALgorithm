## making trail 함수 안에서 델타 탐색 하고 있는 함수

check = True
def making_trail(r,c):
    global cnt
    global max_cnt
    global check

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if is_valid(nr,nc,N):

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