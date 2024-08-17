###진짜
# 34+5+6+7+

# 중위표기식(infix) => 후위표기식(postfix)
# infix : 후위표기식으로 바꿀 중위표기식
# n : 식의 길이
def get_postfix(infix, n):
    # 결과로 출력할 후위표기식
    postfix = ""
    stack = []

    # 문자열에서 하나씩 떼어와서 식 만들자
    for i in range(n):
        # infix[i] => 중위표기식의 i번째 글자
        if infix[i] != "+":
            # i번째 글자가 피연산자다 => 결과에 출력
            postfix += infix[i]
        else:
            while stack:
                postfix += stack.pop()
            stack.append(infix[i])

    # 스택에 남은 연산자 모두 출력
    while stack:
        postfix += stack.pop()

    return postfix

# 후위표기식을 계산하는 함수
def get_result(postfix):
    stack = []

    # 후위표기식에서 글자 하나씩 떼어오기
    for token in postfix:

        # 떼어온 토큰이 피연산자이면 스택에 넣기
        if token != "+":
            stack.append(int(token))  # 타입 조심
        # 토큰이 연산자인 경우 연산에 필요한 만큼 스택에서 피연산자를 꺼낸 후 연산
        # 이 연산 결과를 다음 연산자가 또 써야 하기 때문에 다시 stack에 push
        else:
            # 오른쪽 피연산자가 먼저 나온다
            right = stack.pop()
            left = stack.pop()
            # 계산 결과
            result = left+right
            # 계산 결과를 다음 연산자가 써야하니까 스택에 다시 push
            stack.append(result)

    # 계산이 다 끝나면 스택 안에는 결과가 하나 남아있을 것이다
    return stack.pop()

for tc in range(1, 11):
    N = int(input())
    infix = input()
    postfix = get_postfix(infix, len(infix))
    result = get_result(postfix)
    print(f"#{tc} {result}")