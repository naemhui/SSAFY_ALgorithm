# ```python
# 4
# ( )( )((( )))
# ((( )((((( )( )((( )( ))((( ))))))
# ())
# (()
# ```

T = int(input())

for tc in range(1, T+1):
    check = input()

    stack = []

    # 괄호 검사 결과: 1이면 ok, 0이면 error

    answer = 1

    # 괄호 검사
    # check에서 한 글자씩 떼어와서 검사
    for c in check:
        if c == '(':  # 1. c가 여는 괄호인가?(왼쪽) = > 스택에 push
            stack.append(c)
        if c == ')':  # 2. c가 닫는 괄호인가?(오른쪽) => 스택이 비어있나 확인 => 스택이 비어있으면 err(오른쪽 괄호가 더 많다고 판단)
            if not stack:
                answer = 0
                break  # 이제 볼 필요 없으니 break

        # 스택 안에 뭔가 있으면 꺼내와서 괄호 짝이 맞나 검사
        # 괄호의 종류가 다르면 err  (물론 tc에는 소괄호밖에 없지만 해봐)
        left = stack.pop()
        if not (left == '(' and c == ')'):
            answer = 0
            break

    # 문자열 검사 완료 후 스택이 비어있지 않으면 err
    # if len(stack) > 0
    if stack:
        answer = 0

    print(f'#{tc} {answer}')