# level과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(palindrome)이라 한다.
# 단어를 입력받아 회문이면 1을 출력하고 아니라면 0을 출력하는 프로그램을 작성하라
#
# for i : 0 -> M//2 - 1
#     if s[i] != s[N-1-i]:
#             return 0
#     return 1


T = int(input())
for tc in range(1, T+1):
    s = input()
    N = len(s)
    ans = 1

    for i in range(N//2):
        if s[i] != s[N-1-i]:
            # break 하지 말고
            ans = 0
            break  # 1인 상태 유지하며 출력이 될 것,,?...?

    print(f'#{tc} {ans}')