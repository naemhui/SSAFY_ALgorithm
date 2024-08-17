result = 0

T = int(input())
for tc in range(1, T+1):
    # 문제에서 원하는 답
    answer = 0

    N, M = map(int, input().split())

    # 테스트 케이스 두 번째 줄은 몇 개가 들어올지 모르니까 리스트로 받자
    numbers = list(map(int, input().split()))

    max_sum = 0  # 구간합이 가장 큰 것
    min_sum = 10000*M  # 구간합이 가장 작은 것

    # 반복을 하면서 구간합 구하기
    # N=M+1의 의미는 내가 구간합을 정하는 기준
    # 시작점이 맨앞에서 시작 -> i=0, i=1... i가 몇 까지 갈 수 있는가?
    # 합을 구할 수 있는 i까지만 반복하기 위해
    for i in range(0, N-M+1):
        sub_sum = 0
        # 구간의 시작이 i일 때 구간의 길이가 M이라 하면
        # i  i+1  i+2  ...i+m-1
        # i에서부터 M만큼 가면서 구간합 구해줌 (누적)
        # 내가 구간합에 더할 원소의 위치는? i+j
        for j in range(M):
            # 구간합 구하기
            sub_sum += numbers[i+j]

            # 구간합 다 구하고 나서 최댓값 최솟값 구하기
            max_sum = sub_sum if sub_sum > max_sum else max_sum
            min_sum = sub.sum if sub_sum < min_sum else min_sum

    answer = max_sum - min_sum

    print(f'#{tc} {answer}')

