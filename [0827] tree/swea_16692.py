def in_order(t):  # 인덱스가 들어감
    global word, num
    if t:
        in_order(left[t])

        # t번 인덱스의 word에 숫자 하나씩 증가시키며 넣음
        word[t] = num
        num += 1

        in_order(right[t])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    left = [0]*(n+1)
    right = [0]*(n+1)
    word = [0]*(n+1)

    num = 1

    for i in range(2, n+1):
        parent = i//2

        if left[parent] == 0:
            left[parent] = i
        else:
            right[parent] = i

    in_order(1)
    print(f'#{tc} {word[1]} {word[n//2]}')