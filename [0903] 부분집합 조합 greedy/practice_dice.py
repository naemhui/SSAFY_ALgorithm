arr = [1, 2, 3, 4, 5, 6]
path = []
n = 3

def dice_roll(lev, start):
    if lev == n:
        print(*path)
        return

    for i in range(start, 6):
        path.append(arr[i])
        dice_roll(lev+1, i)
        path.pop()

dice_roll(0, 0)