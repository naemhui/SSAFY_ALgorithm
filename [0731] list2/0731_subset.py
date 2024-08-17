# number_set의 부분집합들을 subset_list에 append 후, 조건을 만족하는 subset을 count
def subset(number_set, n, k):
    N = len(number_set)
    subset_list = []
    count = 0

    for i in range(1, 1<<N):
        subset = []

        # 이제 부분집합 만들 거임
        for j in range(N):
            if i & (1 << j):
                subset.append(number_set[j])
        subset_list.append(subset)
    # print(len(subset_list))

    for subset in subset_list:
        if len(subset) == n:  # 부분집합 원소의 개수 == n
            if sum(subset) == k:  # 원소의 합 == k
                count += 1
    
    return count


T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    number_set = list(range(1, 13))
    # subset(number_set, n, k)
    result = subset(number_set, n, k)
    print(f'#{tc+1} {result}')