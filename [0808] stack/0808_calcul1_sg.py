for tc in range(1, 11):  # 테스트케이스 10개 반복
    n = int(input())  # 문자열 계산식의 길이 입력
    infix = list(input())  # 문자열 입력


    def get_postfix(infix, n):  # 중위표기식을 후위표기식으로 만들기위한 함수 정의
        postfix = list("")  # 후위표기식을 입력받기 위해 비워두고 설정
        stack = []  # + 연산자를 저장하기 위해 스택 생성

        for i in range(n):  # 문자열의 길이만큼 반복
            if infix[i] != "+":  # i번쨰에서 +를 만나지 않은 경우
                postfix += infix[i]  # postfix에 i(숫자)를 추가

            else:  # if 이외에(+를 만난 경우)
                while stack:  # 스택에 +가 있는 경우
                    postfix += stack.pop()  # postfix에 스택을 pop한다(+를 추가)

                stack.append(infix[i])  # 스택에 +가 없는 경우
                # 스택에 infix[i](+)를 추가한다

        while stack:  # 반복문이 끝난 후 스택이 차있는 경우(+)가 들어있는 경우
            postfix += stack.pop()  # 스택의 +를 postfix에 추가한다

        return ''.join(postfix)  # 리스트에서 []와 ''를 지우고 숫자와 연산자만 return하기 위해 ''.join사용
        # '+'.join의 경우 숫자와 연산자들 사이에 +가 추가된 채로 return


    postfix = get_postfix(infix, n)  # 후위연산자로 만든 것을 postfix로 설정


    def get_result(postfix):  # postfix의 값을 만들기 위한 함수 정의
        stack = []  # 숫자를 저장하기 위해 stack 생성

        for token in postfix:  # postfix에서 token을 반복
            if token != "+":  # token이 +가 아닌 경우
                stack.append(int(token))  # int형으로 토큰을 스택에 추가한다.
                # 후위로 만드는 과정에서 ''join으로 str형태가 되었기에
                # 숫자는 int형으로 변환하여 stack에 추가

            else:  # if가 아닌 경우
                left = stack.pop()  # 왼쪽을 stack에서 pop
                right = stack.pop()  # 오른쪽을 stack에서 pop

                result = 0  # 왼쪽 + 오른쪽을 더하기 위해 결과값을 0으로 설정

                if token == "+":  # token이 +인 경우
                    result = left + right  # 왼쪽 + 오른쪽을 더하고 result에 추가

                    # 이 경우 +만 있기에 왼쪽 오른쪽 신경 안 씀
                    # 다른 연산자가 있을 경우 양쪽을 신경써야한다.

                stack.append(result)  # result를 stack에 추가한다.

        return stack.pop()  # 반복문이 끝난 후 stack값을 반환한다.


    result = get_result(postfix)  # return한 값을 결과값으로 설정

    print(f"#{tc} {result}")  # 결과값 출력