# # 무방향
# def dfs_m(s, V):
#     # 방문 체크
#     visited = [0] * (V + 1)
#     # 다시 돌아올 정점 번호를 저장할 스택
#     stack = []
#     # 시작 정점은 방문 처리
#     visited[s] = 1
#     print(s)  # 시작 정점 출력
#     # 현재 방문하고 있는 정점
#     v = s
#
#     while True:
#         # 현재 정점(v)에서 방문할 수 있는 정점 찾기
#         for i in range(1, V+1):
#             # v정점에서 i정점으로 가는 길이 있고 i정점을 방문한 적이 없는지 검사
#             if adj_m[v][i] == 1 and visited[i] == 0:
#                 # 돌아올 곳(현재 정점)을 스택에 저장
#                 stack.append(v)
#                 print(i)  # 방문한 정점 출력
#                 visited[i] = 1  # 방문 체크
#
#                 # 현재 정점을 i로 변경하고 다시 탐색 시작
#                 v = i
#                 break
#         else:
#             # 현재 정점 v에서 갈 수 있는 정점을 찾지 못했을 때
#             if stack:
#                 # 스택에 정점이 있다면 가장 최근에 방문한 정점으로 돌아감
#                 v = stack.pop()
#             else:
#                 # 스택이 비어있다면 모든 탐색이 끝난 것
#                 break
#
#
# # 입력 처리 및 인접 행렬 생성
# V, E = map(int, input().split())
# adj_m = [[0] * (V + 1) for _ in range(V+1)]
#
# for _ in range(E):
#     s, e = map(int, input().split())
#     adj_m[s][e] = 1
#     adj_m[e][s] = 1  # 무방향 그래프의 경우
#
# # DFS 실행 (1번 정점에서 시작)
# dfs_m(1, V)


######유방향
def dfs_m(s, V):
    visited = [0] * (V + 1)
    stack = []
    visited[s] = 1
    print(s)  # 시작 정점 출력
    v = s

    while True:
        for i in range(1, V+1):
            if adj_m[v][i] == 1 and visited[i] == 0:
                stack.append(v)
                print(i)
                visited[i] = 1
                v = i
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

# 입력 처리 및 인접 행렬 생성 (유방향 그래프용)
V, E = map(int, input().split())
adj_m = [[0] * (V + 1) for _ in range(V+1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj_m[s][e] = 1  # 유방향 그래프이므로 한 방향으로만 설정

# DFS 실행 (1번 정점에서 시작)
dfs_m(1, V)









# #### 인덱스
# # s(시작 정점)에서 시작하여 v(현재 정점)과 연결된 정점 확인
# # 방문하지 않은 정점을 발견하면
# # 현재 정점을 스택에 저장(나중에 돌아올 곳) - 새 정점 방문 후 출력
# # - 새 정점을 현재 정점으로 설정 (더 이상 갈 곳 없으면 스택에서 이전 정점 꺼내 돌아감)
# # - 스택이 비어있고 더 이상 갈 곳 없으면 탐색 종료
#
# # 정점 수(V)와 간선 수(E) 입력 받기
# V, E = map(int, input().split())
#
# # 인접 리스트 초기화
# adj_l = [[] for _ in range(V+1)]
#
# # 간선 정보 입력 받기
# for _ in range(E):
#     s, e = map(int, input().split())
#     adj_l[s].append(e)
#     adj_l[e].append(s)  # 무방향 그래프인 경우
#
# def dfs_l(s, V):
#     visited = [0] * (V+1)  # 방문 체크 배열
#     stack = []  # 돌아갈 경로를 저장할 스택
#     visited[s] = 1  # 시작 정점 방문 체크
#     v = s  # 현재 정점
#     print(v)  # 시작 정점 출력
#
#     while True:  # 탐색이 끝날 때까지 반복
#         for i in adj_l[v]:  # 현재 정점과 연결된 모든 정점에 대해
#             if not visited[i]:  # 방문하지 않은 정점이라면
#                 stack.append(v)  # 현재 정점을 스택에 저장 (돌아올 곳)
#                 print(i)  # 새로 방문한 정점 출력
#                 visited[i] = 1  # 방문 체크
#                 v = i  # 현재 정점을 새로 방문한 정점으로 변경
#                 break  # for 루프 탈출
#         else:  # 연결된 모든 정점을 방문했다면
#             if stack:  # 스택이 비어있지 않다면
#                 v = stack.pop()  # 이전 정점으로 돌아감
#             else:  # 스택이 비어있다면
#                 break  # 탐색 종료
#
# # DFS 실행 (1번 정점에서 시작)
# dfs_l(1, V)