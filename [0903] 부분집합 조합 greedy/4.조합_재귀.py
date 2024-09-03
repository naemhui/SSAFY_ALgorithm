'''
arr = ['A', 'B', 'C', 'D', 'E'] 중에 3명 뽑기 - 조합
A B C
A B D
A B E
A C D
A C E
A D E
B C D
B C E
B D E
C D E
'''

arr = ['A', 'B', 'C', 'D', 'E']
path = []
n = 3


def run(lev, start):
    if lev == n:
        # print()
        print(*path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        run(lev + 1, i + 1)
        path.pop()
        # print(' pop을 했다:', path, ' lev:', lev, ' i:', i)

run(0, 0)