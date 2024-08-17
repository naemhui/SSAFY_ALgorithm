# def fact(n):
#     return n*fact(n-1)
#
# print(fact(5))  # 이렇게만 있으면 fact(5) fact(4) ...f(0) ... f(-1)... -> 중단하는 코드 써야대

# def fact(n):
#     if n ==1:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

def f(n):
    global cnt
    cnt += 1
    if n == 0:
        return
    else:
        f(n-1)

cnt = 0
f(1000)
print(cnt)


