# 모든 부분집합을 구하는!!!!!!

lst = [1, 2, 3, 4, 5]
N = 5
print(lst)


# idx : 내가 현재 idx번째 원소를 고를지 말지 선택
# selected : 내가 고른 원소를 체크
# selected[x] == 1 : x번째 원소를 부분집합에 포함시킴
# selected[y] == 0: y번째 원소는 부분집합에 포함하지 않았다.
# n : 원소의 전체 개수
def make_subset(idx, selected, n):

    # 종료 조건
    if idx == n:
        # n 도달 -> 모든 원소 고려했다 -> 부분집합 구하기 완료
        subset = []  # 현재까지 선택된 원소들을 저장할 준비 완료
        for i in range(n):
            # i번째 원소를 골랐으면
            if selected[i]:  # i번째 원소가 현재 부분집합에 포함되어야 한다는 말이므로
                # 부분집합에 넣기
                subset.append(lst[i])  # 그 원소를 subset에 추가함
        print(subset)
        return

    # 재귀 호출 (원소포함)
    # idx번째 원소에 대해 부분집합에 idx원소를 포함시키겠다
    selected[idx] = 1
    # print(f'{idx} {selected} O')
    make_subset(idx+1, selected, n)  # 다음 원소로 넘어가기



    # 재귀 호출 (원소 미포함)
    # 부분집합에 idx번째 원소를 포함시키지 않겠다
    selected[idx] = 0
    # print(f'{idx} {selected} X')
    make_subset(idx+1, selected, n)


make_subset(0, [0]*N, N)