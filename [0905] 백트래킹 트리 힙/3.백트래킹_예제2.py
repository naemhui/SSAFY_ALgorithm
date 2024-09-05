# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
# 단, 순서에 따른 중복을 제거하세요
arr = [i for i in range(1, 11)]
visited = []


# 버전1
def dfs(level, sum, idx):

    ### 기저조건 가지치기: 문제에서 발견하기 힘든 경우가 많음
    # 가지치기 : 합이 10이면 종료
    if sum == 10:
        print(*visited)
        return

    # 가지치기 : 10이상의 숫자면 볼 필요 없음
    if sum > 10:
        return
    ##########

    ## 후보군 가지치기: 문제에서 알려주거나 예시 주는 경우가 많음!!!
    for i in range(idx, len(arr)):
        # 가지치기 : 이미 사용한 숫자라면 생략
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i], i)
        visited.pop()


# 버전2
# 1을 썼으면 앞으로는 1을 고려하지 않아도 된다 -> 이런ㄱ ㅔ 이진트리 구조!!!
# 이진 트리 구조처럼 사용하면(후보를 사용하느냐 vs 마느냐) 훨씬 쉽고 빠르다
def dfs2(level, sum):
    if sum > 10:
        return

    if sum == 10:
        print(*visited)
        return

    # 모두 선택하지 않으면 합이 10이 넘지 못하므로
    # 기저조건 추가
    if level == len(arr):
        return

    # 선택하는 경우
    visited.append(arr[level])  # 경로 저장 용.
    dfs2(level + 1, sum + arr[level])  # 방문 체크 안 해도 됨. 무조건 level+1로 하기 때문에 다음 케이스에서 이전 거 고려X
    visited.pop()

    # 현재 숫자를 선택하지 않는 경우
    dfs2(level + 1, sum)


# dfs(0, 0, 0)
dfs2(0, 0)