T = int(input())

for tc in range(1, T+1):
    check = input()

    stack = []
    answer = 1

    for c in check:
        if c == '(' or c == '{':
            stack.append(c)
        if c == ')':
            if not stack:
                answer = 0
                break

            left = stack.pop()
            if left == '{':
                answer = 0
                break

        if c == '}':
            if not stack:
                answer = 0
                break

            if stack[-1] == '(':
                answer = 0
                break
            stack.pop()

    if stack:
        answer = 0

    print(f'#{tc} {answer}')

