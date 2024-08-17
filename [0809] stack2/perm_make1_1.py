# 자리 정하기? 방법

lst = [1, 2, 3, 4, 5]

N = 5

# idx: 현재 순열의 i번째 자리에 올 원소 선택
# selected: 순열을 만들 때 이전에 사용했던 원소 체크(중복 선택 방지)
# result: 지금까지 내가 만든 순열
# n: 순열의 길이
def make_perm(idx, selected, result, n):

    # 종료 조건
    if idx == n:
        # 지금까지 만든 순열 출력
        print(result)
        return

    # 재귀 호출
    # 현재 순열의 idx번째 자리에 놓을 원소 선택
    # 이전에 고른 적이 없는 원소를 자리에 놓아야 함
    # 내가 고를 수 있는 원소는 lst 안에 있음 : lst인덱스 범위: 0~n-1
    for i in range(n):
        # i번 원소를 이전에 고른 적이 업사 -> 순열의 idx번째 자리에 i번 원소를 놓는다.
        if not selected[i]:  # if selected[i] == 0: 이랑 같은 말!
            # i번째 원소 골랐다고 쳌
            selected[i] = 1
            #idx+1번째 자리 원소 정하러 가기
            result.append(lst[i])
            # idx+1번째 자리 원소 정하러 가기
            make_perm(idx+1, selected, result, n)

            # i번째 원소를 원상복귀
            # idx번째 자리에 i+1, i+2..번째 원소를 골라야 할 수도 있으니까
            selected[i] = 0  # 맨 마지막 원소를 방문 안 했다고 하고
            result.pop()  # 마지막 원소 제거도 해줘야 해
            #make_perm() 호출하면 안돼 이거 조합 아니야 순열이야 1 2 _ 4 5 이렇게 비어있음 안돼

make_perm(0, [0]*N, [], N)




# def backtrack(a, k, n):
#     c = [0]*MAXCANDIDATES
#
#     if k == n:
#         for i in range(0, k)
#             print(a[i], end="")
#         print()
#
#     else:
#         ncandidiates = constrack_candidates(a, k, n, c)
#         for i in range(ncandidiates):
#             a[k] = c[i]
#             backtrack(a, k+1, n)
#
# def construct_candidates(a, k, n, c):
#     in_perm = [False]*c[i]