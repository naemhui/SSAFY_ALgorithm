# 1부터 10까지 출력해보기
# 반복문 -> 재귀호출

# n = 10
# for i in range(1, n+1):  # 시작 1, 종료 10, 값 변화량 +1, 값을 나타내기 위해 사용하는 변수 i
#     print(i, end=' ')
# print()
# 시작과 종료값이 중요함. 그리고 값의 변화량

def my_print(j, n):  # 시작 1, 종료 10, 값 변화량 +1, 값을 나타내기 위해 사용하는 변수 j
    if j > n:
        return

    print(j, end=' ')
    # 종료 조건에 점점 가까워지도록 재귀호출 해줘야 함. 인자를 통해 !!!
    return my_print(j+1, n)
my_print(1, 10)