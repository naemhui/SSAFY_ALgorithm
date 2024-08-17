T = int(input())
for test_case in range(1, T + 1):
    K,N,M = map(int,input().split())
    charge = list(map(int,input().split()))
    current_loc = 0
    next_loc = 0
    cnt = 0
    
    while 1:
        if N <= current_loc + K:
            break
        for i in charge:
            if i <= current_loc+K:
                next_loc = i
        if current_loc == next_loc:
            cnt = 0
            break
        current_loc = next_loc
        cnt +=1
    print(f'#{test_case} {cnt}')