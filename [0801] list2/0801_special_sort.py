T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))

    lst = []

    while len(lst) < 10 and data:
        max_val = max(data)
        lst.append(max_val)
        data.remove(max_val)

        if len(lst) == 10 or not data:
            break

        min_val = min(data)
        lst.append(min_val)
        data.remove(min_val)

    print(lst)
