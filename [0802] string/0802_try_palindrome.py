def palindrome(text, n, m):
    for i in range(n):
        for j in range(n-m+1):

            cnt = 0
            for k in range(m//2):
                if text[i][j+k] == text[i][j+m-1-k]:
                    cnt += 1
            if cnt == m//2:
                result = ''.join(text[i][j:j+m])
                return result


    lst = []
    for j in range(n):
        for i in range(n-m+1):
            cnt = 0
            for k in range(m//2):
                if text[i+k][j] == text[i+m-1-k][j]:
                    cnt += 1
    ###################################################
            if cnt == m//2:  # 회문이 맞을 경우
                for r in range(m):  # 회문에 있는 알파벳을
                    lst.append(text[i+r][j])  # 리스트에 추가
                # return result
                # # lst에 값이 다 들어와있음
                result = ''.join(lst)
                return result

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    text = [list(input()) for _ in range(n)]
    result = palindrome(text, n, m)
    print(f'#{tc} {result}')

