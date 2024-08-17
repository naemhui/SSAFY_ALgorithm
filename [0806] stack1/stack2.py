def f2(c, d):
    return c-d

def f1(a, b):
    c = a+b
    d = 10
    return f2(c, d)

a = 10
b = 20
print(f1(a, b))


# python tutor로 확인해보기
# 실행 흐름 확인해보기 stack과 비슷함  이 실행 흐름을 알아야 재귀호출 이해할 수 있다.

a = 10
b = 20

def f1(b, a):
    print('start f1')
    c = a+b
    d = a-b
    print(f2(a, b))

def f2(c, d):
    print('start f2')
    c = 1
    d = 2

    print('end f2')
    return c+d

f1(a, b)
