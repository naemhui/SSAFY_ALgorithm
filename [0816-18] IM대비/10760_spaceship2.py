'''
사진 가능 : 착륙지점보다 높이 낮은 구역
-> 최적의 착륙 장소 정할 수 있음
-> 예비 후보지: 사진 4방향 이상 가능
-> 예비 후보지 개수 출력
'''

## 상1 상2 상3 하1 하2 하3 좌 우
dr = [-1, -1, -1, 1, 1, 1, 0, 0]
dc = [-1, 0, 1, -1, 0, 1, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split(0))
    arr = [list(map(int,input().split())) for _ in range(N)]
    