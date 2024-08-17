T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = input().split('0')

    count = 0

    for i in range(len(data)):
        if len(data[i]) > count:
            count = len(data[i])
    print(f'#{tc} {count}')