# 백트래킹으로 풀어보자
def btrk(n, idx, s, selected):
    global mins
    #혹시 지금까지 합이 최소합보다 크면 뒤는 볼 필요가 없을 것 같아 돌아가줘. (가지치기)
    if s > mins:
        return

#만약 n-1행까지 다 선택하고 idx가 n이 됐으면 최솟값 비교하고 최솟값을 갱신해주자. (종료조건)
    if idx == n:
        if mins > s:
            mins = s
            return

#idx 행에서는 i열의(for문으로 구현) 숫자를 고른 적 없다면 골라볼게. (재귀)
    for i in range(n):
        if not selected[i]:
        #숫자를 골랐으면, i열의 숫자를 다시 고르지 않도록 체크해주자.
            selected[i] = 1
            #고른 숫자는 합계에 더해주자. (자연수니까 계속 커질거야)
            s += arr[idx][i]
            #그리고 idx+1열에서 또 선택하러 가보자.
            #갈 때, 지금까지의 합 (s)과, 골랐던 배열도 같이 가져가줘.
            btrk(n, idx+1, s, selected)

            #보고 왔으면 다음 i도 선택해봐야하니까 골랐던 배열을 지워주자. 합계에서도 빼줘야지!!!
            selected[i] = 0
            s -= arr[idx][i]



T=int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mins = 1000   # 함수에서 계산하면서 변한 걸 출력할게. 아마 최댓값은 크면 900이 가장 클거야
    btrk(N, 0, 0, [0]*N)

    print(f"#{tc} {mins}")