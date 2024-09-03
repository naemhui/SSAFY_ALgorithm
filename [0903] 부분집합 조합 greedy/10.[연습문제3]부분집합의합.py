numbers = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
cnt = 0  # 총 몇가지인지 계산
path = []

# (now: 현재 처리 중인 원소의 인덱스, total: 현재까지 선택된 원소들의 합계)
def recur(now, total):
    global cnt
    if now == 10:
        return

    # 현재까지 선택된 원소들의 합에 현재 원소를 추가했을 때 결과가 0인 경우
    # path와 현재 원소를 더한 리스트를 출력. 이 경우 cnt를 1 증가
    if total + numbers[now] == 0:
        print(path + [numbers[now]])
        cnt += 1

    # 현재 수를 사용하지 않는 경우: 현재 원소 선택하지 않고 다음 원소 처리
    recur(now + 1, total)

    # 현재 수를 사용하는 경우: 경로에 추가, 누적합에 계산
    path.append(numbers[now])
    recur(now + 1, total + numbers[now])
    path.pop()


recur(0, 0)
print(f'총 {cnt}가지')