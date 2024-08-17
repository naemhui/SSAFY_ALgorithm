def HateRepeat(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:  # stack에 데이터가 있고 마지막 원소와 값이 같으면 pop
            stack.pop()
        else:
            stack.append(c)

    return len(stack)

T = int(input())
for tc in range(1, T+1):
    input_str = input().strip()
    print(f'#{tc} {HateRepeat(input_str)}')