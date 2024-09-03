arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']


# path 출력 함수
def print_name():
    print(path, end=' / ')
    print('{ ', end='')
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
    print('}')

def run(lev):
    # 3개를 뽑았을 때 출력
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()

run(0)


###############
# 위 코드가 이해가 안 된다면 아래 코드 참고
###############
# arr = ['O', 'X']
# path = []
# name = ['A', 'B', 'C']
#
#
# def print_name():
#     for i in range(3):
#         if path[i] == 'O':
#             print(name[i], end=' ')
#             # print()
#
#
# def run(lev):
#     if lev == 3:
#         print_name()
#         return
#
#     for i in range(2):
#         path.append(arr[i])
#         run(lev + 1)
#         print()
#         print('pop 전: ', path)
#         path.pop()
#         print('pop 후: ', path)
#
#
# run(0)