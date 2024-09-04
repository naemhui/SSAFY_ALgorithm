# 정렬할 배열의 시작
# 정렬할 배열의 끝

def merge_sort(start, end):

    # 종료 조건
    # 원소가 한 개 있으면 쪼개기 중단
    if start == end-1:
        return start, end

    # 재귀 호출
    # 분할
    # 절반씩 나누기
    # 왼쪽 부분, 오른쪽 부분
    # mid = (start+end) // 2  # 하단의 코드와 결과 같음. 밑의 코드가 다른 언어에서도 쓸 수 잇음
    # 왜냐면 start+end가 너무 커지는 것 방지
    mid = start + (end-start)//2

    # 왼쪽 부분
    left_start, left_end = merge_sort(start, mid)
    # 오른쪽 부분
    right_start, right_end = merge_sort(mid, end)

    # 병합
    merge(left_start, left_end, right_start, right_end)
    return start, end


def merge(ls, le, rs, re):
    # 합친 후 배열의 크기
    n = re - ls

    # 정렬 결과를 저장할 배열
    result = [0]*n
    # idx자리에 왼쪽 부분과 오른쪽 부분의 맨앞 2개 비교
    # -> 더 작은 거 놓을 위치
    idx = 0
    # 왼쪽 부분, 오른쪽 부분 비교해서 작은 것부터
    # result에 넣기


    # 왼쪽 부분 인덱스, 오른쪽 부분 인덱스
    l,r = ls, rs
    # 왼쪽 부분과 오른쪽 부분 둘 다 원소가 있다
    while l < le and r < re:

        # 작은 것부터 놓기
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1  # 다음 비교를 위해 1 증가
            idx += 1  # 다음 위치
        else:
            # 오른쪽이 더 작으면 오른쪽 넣기
            result[idx] = arr[r]
            r += 1
            idx += 1


    # 왼쪽 부분만 있다
    while l < le:
        result[idx] = arr[l]
        l += 1
        idx += 1

    # 오른쪽 부분만 있다
    while r < re:
        result[idx] = arr[r]
        r += 1
        idx += 1


    for i in range(n):
        arr[ls+i] = result[i]

arr = [69, 10, 30, 2, 16, 8, 31, 22]
merge_sort(0, 7)
print(arr)