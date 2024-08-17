T = int(input())

for tc in range(1, T+1):
    n = int(input())
    C_lst = list(map(int, input().split()))

    cnt = 1
    max_cnt = 1
    for i in range(n-1):
        if C_lst[i+1] > C_lst[i]:
            cnt += 1
            # max_cnt = max(max_cnt, cnt)
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_cnt}')