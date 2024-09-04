def is_square(start, end):
    # 기저 조건: 탐색 범위가 유효하지 않으면 0 반환
    if start > end:
        return 0
    mid = (start + end) // 2
    mid_square = mid ** 2

    # area는 정확히 mid의 제곱
    if mid_square == area:
        return mid

    # area < mid_square이면 넓이는 min**2보다 작은 값
    elif mid_square > area:
        return is_square(start, mid - 1)

    # area > mid_square이면 넓이는 min**2보다 큰 값
    else:
        return is_square(mid + 1, end)


T = int(input())
for tc in range(1, T + 1):
    area = int(input())
    answer = is_square(0, area)
    print(f"#{tc} {answer}")