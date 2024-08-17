def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def comb(n, m):
    return factorial(n + m) // (factorial(n) * factorial(m))

def paper(N):
    n = N//10
    if n % 2 == 0:
        cnt = 2**(n//2)
        # for i in range(n//2):
        for i in range(1, n//2):
            cnt += comb(i, n-i*2)
        return cnt + 1

    else:
        cnt = 2**(n//2) * (n//2-1)
        # for i in range(n//2+1):
        for i in range(1, n//2+1):
            cnt += comb(i, (n-2*i))
        return cnt + 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(paper(N))


###########################1
# def paper(N):
#     dp = [0] * (N + 1)
#
#     dp[0] = 1
#     dp[10] = 1
#
#     for i in range(20, N + 1, 10):
#         dp[i] = dp[i - 10] + dp[i - 20] * 2
#
#     return dp[N]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     print(f"#{tc} {paper(N)}")

###########################2
# def paper(N):
#     n = N // 10
#     dp = [0] * (n + 1)
#
#     # 초기 조건 설정
#     dp[0] = 1  # 20x0 크기의 직사각형을 채우는 방법은 1가지 (아무 것도 안 놓는 경우)
#     if n >= 1:
#         dp[1] = 1  # 20x10 크기의 직사각형을 채우는 방법은 1가지 (10x20 타일 하나)
#     if n >= 2:
#         dp[2] = 3  # 20x20 크기의 직사각형을 채우는 방법은 3가지 (20x20 타일 하나 또는 10x20 타일 두 개)
#
#     # DP 점화식 적용
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2] * 2
#
#     return dp[n]
#
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
#
#
# def comb(n, m):
#     return factorial(n + m) // (factorial(n) * factorial(m))
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     print(f"#{tc} {paper(N)}")
