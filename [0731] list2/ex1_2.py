# 반드시 혼자 풀 수 있을 정도가 되어야 함!!!!!!!!!!
# 5*5 배열에 25개의 숫자를 저장하고, 25개의 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절댓값을 구하자
# 예를 들어 아래 그림에서 7값의 이웃한 값은 2 6 8 12이며 차의 절댓값의 합은 12이다.
# 25개의 요소에 대해 모두 조사하여 총합을 구하시오
# 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.
import sys
sys.stdin = open('in.txt', 'r')

# 델타 배열
# 상 > 하 > 좌 > 우
# 0    1    2    3
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 좌표 검사 함수
def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 모든 위치를 탐색하면서
    # 모든 위치에서 상하좌우 요소를 가져온 다음, 차 구하기

    # 모든 위치의 절댓값 합
    diff_sum = 0

    for i in range(N):
        for j in range(N):
            # 행 번호 i, 열 번호 j
            # (i, j) 위치에서 상하좌우 차이 구하기
            now_diff_sum = 0

            # 상하좌우 반복
            for d in range(4):
                ni = i + di[d]  # 현재 위치 i에서 d 방향으로 갔을 때 i의 변화량
                nj = j + dj[d]  # 현재 위치 j에서 d 방향으로 갔을 때 j의 변화량

                # 여기서 바로 하면 안됨
                # 우리가 계산한 다음 위치가 유효한 인덱스인지 반드시 검사!!
                if is_valid(ni, nj):
                # if 0<=ni < N and 0 <= nj < N 이렇게 검사해도 됨
                    diff = abs(arr[i][j] - arr[ni][nj])  # if diff < 0: diff = -diff 
                    
                    # ni, nj가 유효한 위치일 때 절댓값 합 더하기                    
                    now_diff_sum += diff
            
            diff_sum += now_diff_sum

    print(f'#{tc} {diff_sum}')