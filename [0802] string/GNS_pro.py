T = int(input())

for tc in range(1, T+1):
    N = int(input())


    count = [0]*10
    for num in text:
        for i in range(10):
            if num == numbers[i]:
                count[i] += 1

    answer = "" # 빈 문자열 하나 만들어놓고 문자열 + 로 조합헤서 테케 끝난 후 한 번만 출력

    for i in range(10):
        answer = answer + (numbers[i] + " ") * count[i]

    print(f'#{tc} {answer}')