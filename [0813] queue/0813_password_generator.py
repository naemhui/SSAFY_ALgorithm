for t in range(10):
    N = input()  # 테스트케이스 번호
    cq = list(map(int, input().split()))
    size = len(cq)  # 8

    front = rear = 0
    cycle = 1  # 사이클 감소 값

    while True:
        cq[front] -= cycle
		
        # 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지
        if cq[front] <= 0:
            cq[front] = 0
            break

        front = (front + 1) % size
        rear = (rear + 1) % size

        # 사이클이 1~5 반복
        cycle += 1
        if cycle > 5:
            cycle = 1

    print(f'#{N}', end=" ")
    
    # 마지막 위치에 0이 오도록 해야 함
    front = (front+1) % size  # 마지막으로 감소한 위치의 다음 원소부터 출력
    for _ in range(size):
        print(cq[front], end=" ")
        front = (front + 1) % size
    print()


    # result = cq[front:] + cq[:front]
    # print(f'#{N} {" ".join(map(str, result))}')