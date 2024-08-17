def fibol(n):
    # global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibol(n-1 + fibol(n-2)
    return memo(n)

def fibo(n):
    if n <2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = 900
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibo(n))