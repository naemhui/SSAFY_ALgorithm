def backtrack(row, n, now_sum, visited):
    global min_sum
    if row == n:  # i가 배열의 수와 일치하면
        # 현재 합 vs 지금까지의 최소합
        if now_sum < min_sum:
            min_sum = now_sum
    
    # 가지치기
    elif now_sum > min_sum:
        return  # 탐색 중지
    
    else:
        for col in range(n):
            if not visited[col]:  # 방문 전
                visited[col] = 1  # 방문

                # 재귀호출
                # 다음 row로 넘어감 -> now_sum에 값 더함 -> visited 갱신
                backtrack(row+1, n, now_sum+num[row][col], visited)
                visited[col] = 0  # 함수 적용 후 초기화(재검색 할 수 있도록)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 100  # 값을 대체
    visited = [0]*n

    backtrack(0, n, 0, visited)
    print(f'#{tc} {min_sum}')