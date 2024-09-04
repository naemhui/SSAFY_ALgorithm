arr = [2, 4, 7, 9, 11, 19, 23]
# 이진 탐색은 정렬된 데이터에 적용 가능하다.
# arr.sort()

# low: 탐색할 범위의 시작 인덱스  high: 탐색할 범위의 끝 인덱스  cnt: 탐색 횟수 카운트
def binary_search(target):
    low = 0
    high = len(arr) - 1
    # 탐색 횟수 카운팅
    cnt = 0

    while low <= high:  # 탐색 범위에 확인하지 않은 요소가 아직 남아있다
        mid = (low + high) // 2  # 중앙값
        cnt += 1  # 탐색 횟수 +1

        if arr[mid] == target:  # 중앙값 == 찾고자 하는 값이라면
            return mid, cnt

        elif arr[mid] > target:  # 왼쪽을 확인해야 한다 = high 값을 mid-1로 설정
            high = mid - 1
        else:  # 오른쪽을 확인해야 한다 = low 값을 mid+1로 설정
            low = mid + 1

    # 값이 리스트에 없으면 루프 종료
    return -1, cnt

# 인덱스, 탐색 횟수
print(f'9 = {binary_search(9)}')
print(f'2 = {binary_search(2)}')
print(f'20 = {binary_search(20)}')

